# Internal Layer
from generation import generate_prompt
from generation import call_openai
import asyncio
import data
import parameters
import utils
import time

async def think():
    print("Thinking...")
    i = 0
    while i < 20:
        if not data.locked:
            data.locked = True
            i += 1
            working_memory = data.getWorkingMemory(1)
            internalmem = data.getMemory(1)
            # Need to fix memory access
            prompt = generate_prompt("internal/step_conscious", (internalmem, working_memory, ))
            ai_response = call_openai(prompt, 32, temp = 0.85)
            prompt = generate_prompt("internal/integrate", (internalmem, working_memory, ai_response, utils.internalLength(), parameters.requirements, ))
            output = await asyncio.get_event_loop().run_in_executor(None, utils.updateInternal, 1, prompt, parameters.internal_capacity)
            working_memory += ai_response + "\n"

            data.setWorkingMemory(1, working_memory)
            print(str(round(i * 100 / 20 )) + "% complete...")
            data.locked = False
            await asyncio.sleep(parameters.thinkpause)
        await asyncio.sleep(0)

# Run simultaneous internal monologues, without access to system resourcs, and which does not receive notifications from external info.
lastsub = 0
async def subthink():
    global lastsub
    # Subcount of zero means no running subconscious.
    if parameters.subs == 0:
        return

    while True:
        if not data.locked:
            data.locked = True
            working_memory = data.getWorkingMemory(lastsub + 2)
            internalmem = data.getMemory(1)
            merged_memory = internalmem
            # Started adding code for subconscious persistent memory
            existingmem = data.getMemory(lastsub + 2)
            if existingmem is not None:
                prompt = generate_prompt("merge", (internalmem, existingmem, ))
                merged_memory = call_openai(prompt, round((parameters.internal_capacity + parameters.sub_capacity) / 2))
            prompt = generate_prompt("internal/step_subconscious", (merged_memory, working_memory, ))
            ai_response = call_openai(prompt, 32, temp = 0.9)
            if existingmem is not None:
                prompt = generate_prompt("internal/integrate", (existingmem, working_memory, ai_response, utils.subLength(), parameters.requirements, ))
                await asyncio.get_event_loop().run_in_executor(None, utils.updateInternal, (lastsub + 2), prompt, parameters.sub_capacity)
            else:
                prompt = generate_prompt("internal/bootstrap_sub", (internalmem, ai_response, utils.subLength()))
                mem = call_openai(prompt, parameters.sub_capacity)
                data.appendMemory(mem)
                data.appendHistory(lastsub + 2, mem)
            # Integrate into internal memory.
            prompt = generate_prompt("internal/integrate", (internalmem, working_memory, ai_response, utils.internalLength(), parameters.requirements, ))
            await asyncio.get_event_loop().run_in_executor(None, utils.updateInternal, 1, prompt, parameters.internal_capacity)
            # Crashes around here on lastsub == 9
            working_memory += ai_response + "\n"

            data.setWorkingMemory(lastsub + 2, working_memory)

            # Cycle through subconsciousness
            lastsub += 1
            if lastsub == parameters.subs:
                lastsub = 0

            data.locked = False
            await asyncio.sleep(parameters.subpause)
        await asyncio.sleep(0)
