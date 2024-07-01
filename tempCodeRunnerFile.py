import matplotlib.pyplot as plt

# Define the age measurements with categories
age_measurements = {
    # Brain
    "White Matter Hyperintensities": 48,
    "Pineal calcification": 40,
    "Ventricular volume": 48,
    "Cortical grey volume": 45,
    "AI T1 brain age": 44,
    "RAVENS PM": 41,
    "Total Cerebral WMV": 37,
    "WASO": 37,

    # Heart
    "Resting Heart Rate": 40,
    "HRV (heart)": 40,
    "VO2Max (heart)": 18,
    "LV septal A’ mitral": 70,
    "Aortic root diameter": 70,
    "LA E’ latbasal": 70,
    "RVSP": 70,
    "LV sepal E/E’": 55,
    "RV E/A": 52,
    "LV E/A": 28,
    "RCCA PSEM": 26,
    "LCCA PSEM": 18,
    "Common carotid average intima media thickness": 32,
    "Internal carotid artery maximum intima media thickness": 25,
    "Intraventricular relaxation time (IVRT)": 19,
    "E/A pulsed wave doppler in the mitral valve": 28,
    "Tissue doppler (septal LV E’ mitral annulus speed)": 24,
    "Blood urea nitrogen": 21,
    "MaxHR": 37,
    "Waist circumference": 25,
    "BIA scale body fat": 16,
    "Pulse Wave Velocity": 30,

    # Kidney
    "Renal interlobar arteries resistive index (right)": 25,
    "Renal interlobar arteries resistive index (left)": 25,

    # Lungs
    "FEV1": 22,
    "FVC": 26,
    "PEFR": 33,
    "DLCOc": 38,
    "KCOc": 54,
    "MIP & MEP": 20,

    # Hair
    "grey hair age": 31,
    "Hamilton-Norwood (hair)": 26,
    "Grey+white (hair)": 41,

    # Skin
    "Spots (skin)": 10,
    "Wrinkles (skin)": 10,
    "Texture (skin)": 14,
    "Pores (skin)": 50,
    "UV Spots (skin)": 62,
    "Brown spots (skin)": 11,
    "Red areas (skin)": 70,
    "Autofluorescence (skin)": 32,
    "Multispectral imaging face": 41,

    # Eyes
    "Sub-foveal choroidal thickness": 51,
    "Enhanced depth imaging": 70,
    "IOP": 38,
    "Eyelash length": 70,

    # Ears
    "Right ear normal freq": 61,
    "Left ear normal freq": 51,
    "Right ear EHF": 60,
    "Left ear EHF": 32,

    # Sensory nervous system
    "Sensory nervous system measurements": 30,

    # General
    "chronological age at goal achievement": 30,
    "Speed of aging": 20,
    "Body inflammation": 18,
    "VO2 max": 18,
    "Total Bone Mineral Density": 30,
    "Nighttime erections": 18,
    "HRV": 12,
    "Alpha Klotho biological age": 21,
    "Free testosterone index (FTI)": 20,
}

# Define color mapping for categories
color_mapping = {
    'Brain': 'blue',
    'Heart': 'red',
    'Kidney': 'green',
    'Lungs': 'orange',
    'Hair': 'purple',
    'Skin': 'brown',
    'Eyes': 'cyan',
    'Ears': 'magenta',
    'Sensory nervous system': 'yellow',
    'General': 'grey'
}

# Assign categories to each measurement
categories = {
    "White Matter Hyperintensities": 'Brain',
    "Pineal calcification": 'Brain',
    "Ventricular volume": 'Brain',
    "Cortical grey volume": 'Brain',
    "AI T1 brain age": 'Brain',
    "RAVENS PM": 'Brain',
    "Total Cerebral WMV": 'Brain',
    "WASO": 'Brain',

    "Resting Heart Rate": 'Heart',
    "HRV (heart)": 'Heart',
    "VO2Max (heart)": 'Heart',
    "LV septal A’ mitral": 'Heart',
    "Aortic root diameter": 'Heart',
    "LA E’ latbasal": 'Heart',
    "RVSP": 'Heart',
    "LV sepal E/E’": 'Heart',
    "RV E/A": 'Heart',
    "LV E/A": 'Heart',
    "RCCA PSEM": 'Heart',
    "LCCA PSEM": 'Heart',
    "Common carotid average intima media thickness": 'Heart',
    "Internal carotid artery maximum intima media thickness": 'Heart',
    "Intraventricular relaxation time (IVRT)": 'Heart',
    "E/A pulsed wave doppler in the mitral valve": 'Heart',
    "Tissue doppler (septal LV E’ mitral annulus speed)": 'Heart',
    "Blood urea nitrogen": 'Heart',
    "MaxHR": 'Heart',
    "Waist circumference": 'Heart',
    "BIA scale body fat": 'Heart',
    "Pulse Wave Velocity": 'Heart',

    "Renal interlobar arteries resistive index (right)": 'Kidney',
    "Renal interlobar arteries resistive index (left)": 'Kidney',

    "FEV1": 'Lungs',
    "FVC": 'Lungs',
    "PEFR": 'Lungs',
    "DLCOc": 'Lungs',
    "KCOc": 'Lungs',
    "MIP & MEP": 'Lungs',

    "grey hair age": 'Hair',
    "Hamilton-Norwood (hair)": 'Hair',
    "Grey+white (hair)": 'Hair',

    "Spots (skin)": 'Skin',
    "Wrinkles (skin)": 'Skin',
    "Texture (skin)": 'Skin',
    "Pores (skin)": 'Skin',
    "UV Spots (skin)": 'Skin',
    "Brown spots (skin)": 'Skin',
    "Red areas (skin)": 'Skin',
    "Autofluorescence (skin)": 'Skin',
    "Multispectral imaging face": 'Skin',

    "Sub-foveal choroidal thickness": 'Eyes',
    "Enhanced depth imaging": 'Eyes',
    "IOP": 'Eyes',
    "Eyelash length": 'Eyes',

    "Right ear normal freq": 'Ears',
    "Left ear normal freq": 'Ears',
    "Right ear EHF": 'Ears',
    "Left ear EHF": 'Ears',

    "Sensory nervous system measurements": 'Sensory nervous system',

    "chronological age at goal achievement": 'General',
    "Speed of aging": 'General',
    "Body inflammation": 'General',
    "VO2 max": 'General',
    "Total Bone Mineral Density": 'General',
    "Nighttime erections": 'General',
    "HRV": 'General',
    "Alpha Klotho biological age": 'General',
    "Free testosterone index (FTI)": 'General',
}

# Filter out "various" entries and convert the ages to a list of tuples for plotting
plot_data = [(k, v) for k, v in age_measurements.items() if isinstance(v, int)]

# Unpack the tuples into two lists and get corresponding colors
organs, ages = zip(*plot_data)
colors = [color_mapping[categories[organ]] for organ in organs]

# Create the plot
plt.figure(figsize=(14, 10))
scatter = plt.scatter(ages, organs, color=colors)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(x=18, color='red', linestyle='--', linewidth=0.5)
plt.axvline(x=100, color='red', linestyle='--', linewidth=0.5)
plt.title('Age measurements on a 1D Scale')
plt.xlabel('Age')
plt.xticks(range(18, 100, 10))
plt.yticks(range(len(organs)), organs)
plt.grid(True, linestyle='--', linewidth=0.5)

# Adjust layout to give more space for y-axis labels
plt.tight_layout(pad=3.0)

# Create a custom legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=category) for category, color in color_mapping.items()]
plt.legend(handles=handles, title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')


plt.show()
