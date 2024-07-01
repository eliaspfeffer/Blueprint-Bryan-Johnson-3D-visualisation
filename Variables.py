age_measurements = {
    # Brain
    "White Matter Hyperintensities": 48,  # White matter hyperintensities are areas of high intensity on MRI scans of the brain indicating small vessel disease.
    "Pineal calcification": 40,  # Pineal gland calcification can affect melatonin production.
    "Ventricular volume": 48,  # Volume of the brain's ventricles, which can increase with age.
    "Cortical grey volume": 45,  # Volume of the brain's cortex, responsible for many higher-order functions.
    "AI T1 brain age": 44,  # An AI-based estimate of the brain's age based on MRI.
    "RAVENS PM": 41,  # A cognitive function test.
    "Total Cerebral WMV": 37,  # Total white matter volume in the brain.
    "WASO": 37,  # Wake After Sleep Onset, a measure of sleep quality.

    # Heart
    "Resting Heart Rate": 40,  # A measure of cardiovascular health and fitness.
    "HRV (heart)": 40,  # Heart Rate Variability, an indicator of autonomic nervous system function and heart health.
    "VO2Max (heart)": 18,  # Maximum oxygen uptake during exercise, indicating cardiovascular fitness.
    "LV septal A’ mitral": 70,  # A measure of left ventricular function.
    "Aortic root diameter": 70,  # Diameter of the aortic root, can increase with age and affect heart function.
    "LA E’ latbasal": 70,  # A measure of left atrial function.
    "RVSP": 70,  # Right Ventricular Systolic Pressure, an indicator of pulmonary artery pressure.
    "LV sepal E/E’": 55,  # A measure of left ventricular function.
    "RV E/A": 52,  # A measure of right ventricular function.
    "LV E/A": 28,  # A measure of left ventricular diastolic function.
    "RCCA PSEM": 26,  # Pressure Strain Elastic Modulus of the right common carotid artery.
    "LCCA PSEM": 18,  # Pressure Strain Elastic Modulus of the left common carotid artery.
    "Common carotid average intima media thickness": 32,  # Thickness of the carotid artery walls.
    "Internal carotid artery maximum intima media thickness": 25,  # Maximum thickness of the internal carotid artery walls.
    "Intraventricular relaxation time (IVRT)": 19,  # Time for the left ventricle to relax after contraction.
    "E/A pulsed wave doppler in the mitral valve": 28,  # Measure of blood flow through the mitral valve.
    "Tissue doppler (septal LV E’ mitral annulus speed)": 24,  # Speed of the septal movement of the left ventricle.
    "Blood urea nitrogen": 21,  # Indicates kidney function and protein intake.
    "MaxHR": 37,  # Maximum heart rate achieved during exercise.
    "Waist circumference": 25,  # Indicator of abdominal fat and overall health.
    "BIA scale body fat": 16,  # Body fat percentage measured by Bioelectrical Impedance Analysis.
    "Pulse Wave Velocity": 30,  # Measure of arterial stiffness.

    # Kidney
    "Renal interlobar arteries resistive index (right)": 25,  # Indicates blood flow resistance in the right kidney.
    "Renal interlobar arteries resistive index (left)": 25,  # Indicates blood flow resistance in the left kidney.

    # Lungs
    "FEV1": 22,  # Forced Expiratory Volume in 1 second, a measure of lung function.
    "FVC": 26,  # Forced Vital Capacity, total amount of air exhaled during the FEV test.
    "PEFR": 33,  # Peak Expiratory Flow Rate, a measure of how quickly air can be exhaled.
    "DLCOc": 38,  # Diffusing capacity of the lung for carbon monoxide, indicates gas exchange efficiency.
    "KCOc": 54,  # Transfer coefficient of the lung for carbon monoxide, indicating efficiency of gas transfer.
    "MIP & MEP": 20,  # Maximum Inspiratory and Expiratory Pressure, measures of diaphragm strength.

    # Hair
    "grey hair age": 31,  # Biological age estimate based on the amount of grey hair.
    "Hamilton-Norwood (hair)": 26,  # A scale of male pattern baldness.
    "Grey+white (hair)": 41,  # Combined measure of grey and white hair indicating age.

    # Skin
    "Spots (skin)": 10,  # Age estimation based on skin spots.
    "Wrinkles (skin)": 10,  # Age estimation based on wrinkles.
    "Texture (skin)": 14,  # Age estimation based on skin texture.
    "Pores (skin)": 50,  # Age estimation based on pore size.
    "UV Spots (skin)": 62,  # Age estimation based on UV damage spots.
    "Brown spots (skin)": 11,  # Age estimation based on brown spots.
    "Red areas (skin)": 70,  # Age estimation based on red areas.
    "Autofluorescence (skin)": 32,  # Age estimation based on skin autofluorescence.
    "Multispectral imaging face": 41,  # Overall facial age estimation based on multispectral imaging.

    # Eyes
    "Sub-foveal choroidal thickness": 51,  # Thickness of the choroid layer under the retina.
    "Enhanced depth imaging": 70,  # Age estimation based on enhanced depth imaging of the eye.
    "IOP": 38,  # Intraocular pressure, can indicate risk of glaucoma.
    "Eyelash length": 70,  # Age estimation based on eyelash length.

    # Ears
    "Right ear normal freq": 61,  # Hearing age estimation for the right ear at normal frequencies.
    "Left ear normal freq": 51,  # Hearing age estimation for the left ear at normal frequencies.
    "Right ear EHF": 60,  # Hearing age estimation for the right ear at extended high frequencies.
    "Left ear EHF": 32,  # Hearing age estimation for the left ear at extended high frequencies.

    # Sensory nervous system
    "Sensory nervous system measurements": 30,  # Equivalent age for sensory nervous system function.

    # General
    "chronological age at goal achievement": 30,  # Age when a specific life goal was achieved.
    "Speed of aging": 20,  # General measure of the speed of biological aging.
    "Body inflammation": 18,  # Level of body inflammation.
    "VO2 max": 18,  # Maximum oxygen uptake during exercise.
    "Total Bone Mineral Density": 30,  # Density of bones, indicates bone health.
    "Nighttime erections": 18,  # Duration of nighttime erections, an indicator of reproductive health.
    "HRV": 12,  # Heart Rate Variability.
    "Alpha Klotho biological age": 21,  # Biological age based on Alpha Klotho protein levels.
    "Free testosterone index (FTI)": 20,  # Biological age based on free testosterone levels.
}



# Define color mapping for categories
color_mapping = {
    'General': 'grey',
    'Sensory nervous system': 'yellow',
    'Ears': 'magenta',
    'Eyes': 'cyan',
    'Skin': 'brown',
    'Hair': 'purple',
    'Lungs': 'orange',
    'Kidney': 'green',
    'Heart': 'red',
    'Brain': 'blue'
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
