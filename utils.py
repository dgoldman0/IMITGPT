from generation import generate_prompt
from generation import call_openai
import data
import parameters

def checkValidMemory(memory, new_memory):
    try:
        if len(new_memory) < parameters.contraction_tolerance * len(memory):
            print("Fails Basic: " + str(len(new_memory)/len(memory) * 100) + "\n\n")
            return False
        if not (new_memory.endswith(".") or new_memory.endswith("?") or new_memory.endswith("!")):
            print("Cut Off Error\n\n")
            return False
        if not new_memory[0].isupper():
            print("Fails Initial Capitalization\n\n")
            return False
        return True
    except Exception as e:
        print(e)

def updateInternal(mem_id, prompt, capacity):
    print("Updating...\n")
    output = ""
    internalmem = data.getMemory(mem_id)
    while output == "":
        output = call_openai(prompt, capacity)
        final = output

        if mem_id == 1:
            revision_prompt = generate_prompt("internal/revise", (output, internalLength(), ))
            final = call_openai(revision_prompt, capacity)

        if not checkValidMemory(internalmem, final):
            output = ""
    data.setMemory(mem_id, final)
    data.appendHistory(mem_id, final)
    print("Finished...\n")
    return output

# Get the approximate length of memory capacity in words
def internalLength():
    return round(parameters.internal_capacity * 4 / 3.75)

def subLength():
    return round(parameters.sub_capacity * 4 / 3.75)
