import SMSBOMBER

print("Available functions/objects in SMSBOMBER:")
print(dir(SMSBOMBER))

if hasattr(SMSBOMBER, "main"):
    SMSBOMBER.main()
elif hasattr(SMSBOMBER, "start"):
    SMSBOMBER.start()
else:
    print("No main/start function found.")
