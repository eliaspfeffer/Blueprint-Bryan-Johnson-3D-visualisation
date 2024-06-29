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