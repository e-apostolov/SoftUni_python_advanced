from collections import deque

tools_sequence = deque(int(x) for x in input().split())
substance_sequence = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools_sequence and substance_sequence and challenges:
    current_tool = tools_sequence.popleft()
    current_substance = substance_sequence.pop()
    current_value = current_tool * current_substance

    if current_value in challenges:
        challenges.remove(current_value)
    else:
        current_tool += 1
        tools_sequence.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substance_sequence.append(current_substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools_sequence:
    print(f"Tools: {', '.join(str(x) for x in tools_sequence)}")
if substance_sequence:
    print(f"Substances: {', '.join(str(x) for x in substance_sequence)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")
