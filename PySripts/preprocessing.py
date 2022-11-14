import pandas as pd
from statistics import median

def normalize(in_df):
  med_word_brief = median(in_df["[Brief] word count"])
  in_df["[Brief] word count"] = in_df["[Brief] word count"]/med_word_brief
  return in_df


def makes_sense(in_str):
  """
  Assumed any sentence with less than 2 words without numbers is 
  useless.
  """
  word_count = len(in_str.split(" "))
  if word_count<=2:
    for i in in_str:
      if ((i<="9")and(i>="0")):
        return 1
  else:
    return 0
  return 1


def find_cols(in_df):
  fin = ['Website Link', 'App Link', 'Team Size', 'revenue slab',
       'VC funded', 'Angle funding / Seed funding', 'B2B', 'Crowd funded', 'Bootstrapped',
       'Product is not live yet', 'B2C', 'C2C', 'B2B2C', 'Govt. funded', "[Traction] app downloads",
       'Bank funded / Loan', 'Incubator/Accelerator funded', "[Traction] # user",
       'Collected from worksheet',"[Traction] Less than 2" ,"[Brief] word count", 
        "[Traction] More than 2","[Traction] makes sense"]
  fin = {i:[] for i in fin}
  for index, i in in_df.iterrows():
    # website link
    if "www" in str(i["Startup Website"]):
      fin["Website Link"].append(1)
    else:
      fin["Website Link"].append(0)
    # append text in str
    main_str = str(i["Go to Market (in 750 characters)"]) + " "
    main_str += str(i["Describe your company (in 750 characters)"]) + " "
    main_str += str(i["Key Achievements/ Tractions (in 750 characters)"]) + " "
    main_str += str(i["Why do you want to be recognized by TGS100? (in 750 characters)"])
    main_str = main_str.lower()
    # App Link
    if "app" in main_str:
      fin["App Link"].append(1)
    else:
      fin["App Link"].append(0)
    # B2B, B2C, B2B2C, C2C
    find = ["B2B", "B2C", "B2B2C", "C2C"]
    for j in find:
      if j.lower() in main_str:
        fin[j].append(1)
      else:
        fin[j].append(0)
    # VC, Crowd, bootstraped, govt., bank/loan, angle/seed, incubator
    find = {"vc":"VC funded", "crowd": "Crowd funded", "bootstrap":"Bootstrapped",
        "govt":"Govt. funded", "bank":"Bank funded / Loan", "loan":"Bank funded / Loan",
        "angel": "Angle funding / Seed funding", "seed":"Angle funding / Seed funding",
        "incubator":"Incubator/Accelerator funded", "accelerator":"Incubator/Accelerator funded",
        "government":"Govt. funded"}
    for word in find:
      flag = ["VC funded", "Angle funding / Seed funding", "Crowd funded", "Bootstrapped",
            "Govt. funded", "Bank funded / Loan", "Incubator/Accelerator funded"]
      flag = {j:0 for j in flag}
      if word in main_str:
        flag[find[word]] = 1
    for word in flag:
      fin[word].append(flag[word])
    # Team size, num user, collected from sheet
    fin["Collected from worksheet"].append(2022)
    # traction sentence len and makes sense
    traction_str = str(i["Key Achievements/ Tractions (in 750 characters)"])
    word_len = len(traction_str.split(" "))
    if word_len>2:
      fin["[Traction] More than 2"].append(1)
      fin["[Traction] Less than 2"].append(0)
    else:
      fin["[Traction] More than 2"].append(0)
      fin["[Traction] Less than 2"].append(1)
    fin["[Traction] makes sense"].append(makes_sense(traction_str))
    # brief word count
    fin["[Brief] word count"].append(len(str(i["Describe your company (in 750 characters)"]).split(" ")))
    # revenure slab
    num_mapping = {'0- $100,000':40, '$1M - $5M':2454, '$100,000 - $1M':409,
                   'above $5M':4090}
    flag = 0
    for j in num_mapping:
      if j==i["Current Annual Revenue"]:
        fin["revenue slab"].append(num_mapping[j])
        flag = 1
    if flag==0:
      fin["revenue slab"].append(0)
    n_ppl = {'10-50':30, '0-10':5, 'More than 100':100, '50-100':75}

    flag = 0

    for k in n_ppl:
      if k == i["Number of Clients/ Engagements"]:
        fin["[Traction] # user"].append(n_ppl[k])
        flag = 1
    if flag==0:
      fin["[Traction] # user"].append(0)

    flag = 0 

    for k in n_ppl:
      if k == i["Number of Employees"]:
        fin["Team Size"].append(n_ppl[k])
        flag = 1
    if flag==0:
      fin["Team Size"].append(0)

    n_apps = 0
    S = main_str.split(" ")
    for j in range(1,len(S)):
      if S[j] in ["downloaded", "installed", "downloads", "installs"] and ((S[j-1]<="9")and(S[j-1]>="0")):
        try:
          n_apps += float(S[j-1])
        except:
          pass
    fin["[Traction] app downloads"].append(n_apps)

    flag = 0
    for j in range(len(S)):
      if S[j] == "live":
        flag = 0
      else:
        flag=1
    fin["Product is not live yet"].append(flag)

  return normalize(pd.DataFrame(fin))


