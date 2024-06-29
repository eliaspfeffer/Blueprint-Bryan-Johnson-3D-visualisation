#list of organs and their ago:
organs_and_ages = {
    "Heart": 30,
    "Brain": 20,
    "Lungs": 30,
    "Gastrointestinal System": "various",
    "Joints": "various",
    "Hair": "various",
    "Skin": 20,
    "Eyes": "various",
    "Ears": "various",
    "Oral Health": 20,
    "Sleep Quality": 20,
    "Liver": "various",
    "Kidneys": 30,
    "Muscles": 30,
    "Bone Mass": 30,
    "Thymus": "various",
    "Pancreas": "various",
    "Thyroid": 30,
    "Immune System": 30,
    "Reproductive Organs": 30,
    "Blood Vessels": 30,
    "VO2 Max": 30,
    "Skin Age": 20,
    "Nighttime Erections": "various"
}
import matplotlib.pyplot as plt

# Filter out "various" entries and convert the ages to a list of tuples for plotting
plot_data = [(k, v) for k, v in organs_and_ages.items() if isinstance(v, int)]

# Unpack the tuples into two lists
organs, ages = zip(*plot_data)

# Create the plot
plt.figure(figsize=(12, 6))
plt.scatter(ages, organs, color='blue')
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(x=18, color='red', linestyle='--', linewidth=0.5)
plt.axvline(x=120, color='red', linestyle='--', linewidth=0.5)
plt.title('Organ Ages on a 1D Scale')
plt.xlabel('Age')
plt.xticks(range(18, 121, 10))
plt.yticks(range(len(organs)), organs)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()


#When Wifi accessible, ask ChatGPT, to do:
# Now change it to 3D, so I can see how it develops. X achsis = Age, Y achsis = organ name, Z Achsis = time

#Next: Add measurements