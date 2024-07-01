import re

#What this script does:
# 1. Define a Dictionary of Age Measurements: The script starts by defining a dictionary called age_measurements that contains various health metrics and their associated ages.

# 2. Extract Sentences from the Text: The script contains a large block of text which details various health results and metrics. It uses a regular expression to extract all sentences from this text that mention an age.

# 3. Print Extracted Sentences: For each extracted sentence that mentions an age, the script prints the description and the age.

# 4. Compare Extracted Ages with Dictionary: The script then compares the extracted ages with those in the age_measurements dictionary to see if any of the extracted sentences correspond to the metrics defined in the dictionary.

# Store Matches: If a match is found (i.e., if the age in the extracted sentence matches an age in the dictionary and the description contains a keyword from the dictionary), the script stores this match in a list called matches.




# Define the age_measurements dictionary



# Extract all the sentences with age and number from the text
text = """
MY RESULTS FROM 3 yrs of Blueprint:Top 1%: Speed of aging (epigenetic) Top 1%: Muscle mass & functionTop 1%: Fat massTop 1%: Inflammation Top 1%: VO2 max (cardiovascular)Top 1%: Bone massTop 1%: Sleep Top 1%: Combined clinical markers 
+ Speed of aging slower than 99% of 20 year olds
+ Body inflammation is 85% below the average 18 year old (hsCRP 0.15) + VO2 max: 58.7 mL/(kg·min), top 1.5% of 18 year olds
+ Total Bone Mineral Density top .2% of 30 year olds
+ Nighttime erections 179 min, better than ave 18 year old
+ Perfect liver fat (1.36%, top 10%.), iron & stiffness (MRI)  
+  top 99.5% muscle volume+ bottom 0.5% visceral fat, muscle fat, and subcutaneous fat volume 
+ Top 1% sleep performance & recovery (whoop)
+ Possibly increased thymocyte volume to 7 yrs younger, pending further testing
+ Ideal whole body muscle & fat (MRI)+ 50+ optimal clinical outcome biomarkers+ 100+ markers < chronological age+ Perfect liver markers: ALT+AST+GGT = 49
+ Leg press single rep max: 800 lbs.
+ 12 year age reversal in 500 day average HRV 
+ Reduced Alpha Klotho biological age by 21 yrs in 5 months, from 42 to 21.
+ 31 year age reversal in grey hair age (80% reduction in grey hair)+ Identified and corrected (w/o surgery) ticking time bomb: bilateral internal jugular vein (IJV) stenosis

+ 30+ organ ages quantified
+ Free testosterone index (FTI) biological age reduced 20 years

+ Improved homocysteine (hcy) by 49% (5.9 umol/L).
It was 2013 and I’d just sold Braintree Venmo for $800 million in cash, achieving my goal to become independently wealthy by age 30 (I was four years late).
Here is my data after 18 months of adherence
OPTIMAL CLINICAL OUTCOME RANGE

 BIOMARKER                                                                                         RESULT                        AGE EQUIVALENT                                OPTIMAL CLINICAL OUTCOMES  RANGE (OCOR)ALTOPTIMAL18 <15BMIOPTIMAL22.8 <22.5Fasting plasma glucoseOPTIMAL8228 (max reduction)<95Body FatOPTIMAL6.916 (max reduction)<10%Cholesterol (total)OPTIMAL158  DHEAOPTIMAL31025 (max reduction)< age 50Free Testosterone Index OPTIMAL0.441< age 50GGTOPTIMAL10 <14Glutathione OPTIMAL22729< age 30Grip Strength DominantOPTIMAL13433 (max reduction)< age 30Grip Strength Non-dominantOPTIMAL12443 (max reduction)< age 30HbA1COPTIMAL4.528 (max reduction)4.5-5.6HDLOPTIMAL73 50 - 60hsCRPOPTIMAL0.2010 (max reduction)<0.55IGF-1OPTIMAL151 75 - 150LDLOPTIMAL74 < 100NADOPTIMAL52.616 (max reduction)< age 30PSAOPTIMAL0.6822 (max reduction)< age 30RDWOPTIMAL11.318 (max reduction)< age 30SHBGOPTIMAL68  TSHOPTIMAL1.94 1 - 2.1Triglycerides OPTIMAL55 27 - 89Testosterone OPTIMAL76933 (max reduction) VO2 max treadmillOPTIMAL53.618 (max reduction)< age 30WBCOPTIMAL4.5 3.5 - 620th percentile telomeres PBMCOPTIMAL728 (max reduction)< age 30 



MY SPEED OF AGING IS SLOWER THAN 99% OF 20 YEAR OLDS 

My rate of aging is .64 based upon a state of the art epigenetic clock DunedinPACE.
Rotate 6 and 13 mg bi-weekly.17α-E2, 8 mg wk transdermal112 mcg Levothyroxine, 60 mg Armour Thyroid - daily (diagnosed w/ hypothyroidism at age 21).
Upon waking
Acarbose 200 mg (Rx)Ashwagandha 600 mgAstaxanthin 12 mgB Complex .50 pill Mon & Thus (1/2 pill, twice a wk)Boron 2 mgBroccoMax 17.5mg
C 500mgCa-AKG 1 gramCocoa Flavanols 500 mgCoQ10 100 mgD-3 2,000 IUDHEA 25 mgE 67 mgEPA/DHA/DPA 800 mgFisetin 200 mgGarlic 2.4 g equivalentGarlic 1.2 g (kyolic) Genistein 125 mgGinger Root 1.1 gGlucosamine Sulphate 2KCL 1500 mgIodine as potassium iodide 125 mcg K2-MK4, 5 mgK1, 1.5 mgK2 MK-7  600 mcgLithium 1 mgLycopene 10 mgLysine 1 gMetformin ER 1,500 mg (Rx)Nicotinamide Riboside 375 mg
N-Acetyl-L-Cysteine (NAC) 1,800 mgProferrin 10 mgSpermidine 10 mgTurmeric 1 gTaurine 2 g
Viviscal (male) (female) 1 pillZeaxanthin (20 mg Lutein, 4 mg Zeaxanthin) 3x/wkZinc 15 mg
w/Dinner at 11 am
Acarbose 200 mg (Rx)BroccoMax 17.5mgCa-AKG 1 GCocoa Flavanols 500 mg Garlic 2.4 g equivalent 
Garlic 1.2 g (kyolic)Glucosamine Sulphate 2KCL 1,500 mgHyaluronic Acid 300 mg L-Lysine 1g
L-Tyrosine 500 mgMetformin ER 500 mg (Rx)N-Acetyl-L-Cysteine (NAC) 1,800 mgNR 375 mg OR NMN 500 mgTaurine 1 gTurmeric 1 gViviscal (men) (women) 1 pill
Before bed  Melatonin 300 mcg
Other
Extra Virgin Olive Oil, 30 mL daily Pea Protein, 29 grams dailyDark Chocolate, 15 gramsRapamycin (Rx)
wk 1: 13 mg
wk 2: 9 mg
wk 3: 13 mg
wk 4: 9 mg 17α-E2, 8 mg wk transdermalB12 methylcobalamin 1x/wkAspirin 81 mg 3x wk112 mcg Levothyroxine, 60 mg Armour Thyroid (diagnosed with hypothyroidism at age 21)
"""

# Extract all ages and their descriptions from the text
age_sentences = re.findall(r'([a-zA-Z\s\(\)]+) age[s]? (\d+)', text)

# Print the matches
for description, age in age_sentences:
    print(f"Description: {description.strip()}, Age: {age}")

# Compare extracted ages with the age_measurements dictionary
matches = []
for description, age in age_sentences:
    age = int(age)
    description = description.strip()
    for key, value in age_measurements.items():
        if value == age and key in description:
            matches.append((key, value, description))

matches
