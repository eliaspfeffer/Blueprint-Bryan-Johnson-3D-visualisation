organs_and_age_markers = {
    "Heart": "max reduction < age 30",
    "Brain": {
        "Whole brain volume": "younger than chronological age",
        "White matter volume": "younger than chronological age",
        "Cerebral volume": "younger than chronological age",
        "Pituitary brightness": "younger than chronological age",
        "Cerebellar volume": "younger than chronological age",
        "Subcortical grey matter": "younger than chronological age",
        "Ventricular volumes": "younger than chronological age"
    },
    "Lungs": {
        "FEV1": "max reduction < age 30",
        "FVC": "max reduction < age 30",
        "PEFT": "max reduction < age 30",
        "DLCOc": "max reduction < age 30"
    },
    "Gastrointestinal System": "various markers measured",
    "Joints": "various markers measured",
    "Hair": "grey hair reversal",
    "Skin": {
        "Skin Age": "younger than chronological age",
        "Facial left spots": "younger than chronological age",
        "Facial right spots": "younger than chronological age",
        "Facial left texture": "younger than chronological age",
        "Facial right texture": "younger than chronological age",
        "Facial left brown": "younger than chronological age",
        "Facial right brown": "younger than chronological age",
        "Facial left wrinkles": "younger than chronological age",
        "Facial right wrinkles": "younger than chronological age",
        "Facial central spots": "younger than chronological age",
        "Facial central texture": "younger than chronological age",
        "Facial central browns": "younger than chronological age"
    },
    "Eyes": "various markers measured",
    "Ears": "various markers measured",
    "Oral Health": {
        "Calculus index": "younger than chronological age",
        "Recession gingival": "younger than chronological age",
        "Index gingival": "younger than chronological age"
    },
    "Sleep Quality": {
        "Total sleep time": "younger than chronological age",
        "Wake after sleep onset": "younger than chronological age",
        "Sleep efficiency": "younger than chronological age",
        "5 min deep sleep RMSSD": "younger than chronological age"
    },
    "Liver": "various markers measured",
    "Kidneys": {
        "Cystatin C": "max reduction < age 30",
        "eGFR CKD EPI": "max reduction < age 30"
    },
    "Muscles": {
        "Grip strength": "max reduction < age 30",
        "Push up continuity": "max reduction < age 30",
        "Bench press 1 rep max": "max reduction < age 30",
        "Leg press 1 rep max": "max reduction < age 30"
    },
    "Bone Mass": {
        "DEXA L1-4": "max reduction < age 30",
        "DEXA Femur": "max reduction < age 30",
        "DEXA Hip": "max reduction < age 30",
        "Osteocalcin": "max reduction < age 30",
        "Spinal flexibility": "max reduction < age 30"
    },
    "Thymus": "various markers measured",
    "Pancreas": "various markers measured",
    "Thyroid": {
        "TSH": "1 - 2.1",
        "Thyroid volumetrics": "younger than chronological age"
    },
    "Immune System": {
        "hsCRP": "max reduction < 0.55",
        "WBC": "3.5 - 6"
    },
    "Reproductive Organs (including prostate)": {
        "Prostatic volume": "max reduction < age 30",
        "PSA total": "max reduction < age 30",
        "Total testosterone": "max reduction < age 30",
        "Free testosterone index": "max reduction < age 30"
    },
    "Blood Vessels (including internal jugular vein)": {
        "RCCA PSEM": "max reduction < age 30",
        "LCCA PSEM": "max reduction < age 30",
        "RCCA CIMT": "max reduction < age 30",
        "LCCA CIMT": "max reduction < age 30",
        "RICA CIMT": "max reduction < age 30",
        "LICA CIMT": "max reduction < age 30",
        "TPA": "max reduction < age 30",
        "Systolic blood pressure": "max reduction < age 30",
        "Brachial blood pressure": "max reduction < age 30",
        "Non-map C2 CSBP": "max reduction < age 30",
        "Non-map C2 CDBP": "max reduction < age 30",
        "PPA ratio": "max reduction < age 30",
        "AI": "max reduction < age 30",
        "AP": "max reduction < age 30"
    },
    "VO2 Max (Cardiovascular System)": "max reduction < age 30",
    "Skin Age": "younger than chronological age",
    "Nighttime Erections": "various markers measured"
}

# Printing the dictionary to verify
import json
print(json.dumps(organs_and_age_markers, indent=4))

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
