import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

########################################################################################################################

# this script can be used to calculate the stellar mass using the approach described by Zibetti et al. 2009

########################################################################################################################

# Units and definitions
Lsun = 3.846e26 # Solar luminosity in Watt


# Determine g and i band images
images = os.listdir("./SAMPLE/")
gimages = [image for image in images if image.endswith("g.csv")]
iimages = [image for image in images if image.endswith("i.csv")]
ids = [image.split("-")[0] for image in gimages]

# Read in stellar masses and distance
df_mass = pd.read_csv(os.path.abspath("./sample.csv"), sep=';')
df_mass['SDSS_ID'] = df_mass['SDSS_ID'].apply(str)

################################################ Plotting a frame ######################################################

# Read in as pandas dataframe
df_image = pd.read_csv(os.path.abspath("./SAMPLE/" + gimages[15]), sep=',')

# Plot an image with a certain scale
print("plotting image : ", images[15])
plt_data = [[float(y) for y in x] for x in df_image.as_matrix()] # convert to matrix
plt.imshow(plt_data, cmap='gist_heat')
plt.colorbar()
plt.clim(0,1) # set Zscale
plt.show()

############################################ Determine stellar mass ####################################################

gi_masses = []
true_masses = []
errors = []

for ID in ids:

    df_g_image = pd.read_csv(os.path.abspath("./SAMPLE/" + ID + "-g.csv"), sep=',')
    df_i_image = pd.read_csv(os.path.abspath("./SAMPLE/" + ID + "-i.csv"), sep=',')

    flux_g = df_g_image.values.sum()  #add all values in the dataframe
    flux_i = df_i_image.values.sum()

    col_gi = -2.5*np.log10(flux_g/flux_i) # calculate the color difference
    logML_g  = -1.197 + 1.431 * col_gi # calculate the mass-to-light ratio
    ML_g     = 10**logML_g

    flux_g_Jy = flux_g * 3.631e-6 # nanomaggies to jansky
    dist = df_mass[df_mass['SDSS_ID'] == ID]['Distance']
    D = dist * 3.086e22 # Megaparsec to meter

    Lg = flux_g_Jy * 1.e-26 * 4.*np.pi*D**2 * 3.e8 / (0.469*1.e-6) / Lsun # flux to solar luminosity

    Mg = ML_g*Lg # Stellar mass in solar masses

    gi_masses.append(float(np.log10(Mg))) # log10 of stellar mass
    true_masses.append(float(df_mass[df_mass['SDSS_ID'] == ID]['logMstar']))
    errors.append(float(df_mass[df_mass['SDSS_ID'] == ID]['err_logMstar']))

df_comparison = pd.DataFrame({"CalcMass": gi_masses,
                              "TrueMass": true_masses,
                              "Error": errors})
print(df_comparison.head())
print(df_comparison.dtypes)
plt.errorbar(df_comparison['CalcMass'], df_comparison['TrueMass'], yerr=df_comparison['Error'], fmt='o')
plt.xlabel('log g-i colour mass $[M_\odot]$')
plt.ylabel('log SED fit mass $[M_\odot]$')
plt.show()

