import pickle
import pandas as pd
from .config import CLASSIFICADOR, LABELENCONDER_type_school, LABELENCONDER_school_accreditation, LABELENCONDER_gender, LABELENCONDER_interest,  LABELENCONDER_residence, LABELENCONDER_parent_was_in_college

def preprocess(sample):
    print(f'----------------Sample: {sample}')
    with open(LABELENCONDER_type_school, 'rb') as f:
        type_school_encoded = pickle.load(f)
    with open(LABELENCONDER_school_accreditation, 'rb') as f:
        school_accreditation_encoded = pickle.load(f)
    with open(LABELENCONDER_gender, 'rb') as f:
        gender_encoded = pickle.load(f)
    with open(LABELENCONDER_interest, 'rb') as f:
        interest_encoded = pickle.load(f)
    with open(LABELENCONDER_residence, 'rb') as f:
        residence_encoded = pickle.load(f)
    with open(LABELENCONDER_parent_was_in_college, 'rb') as f:
        parent_was_in_college_encoded = pickle.load(f)

    
    df_new_sample = pd.DataFrame(
        columns=['type_school_encoded', 'school_accreditation_encoded', 'gender_encoded', 'residence_encoded', 'parent_was_in_college_encoded'])
    df_new_sample.loc[0, 'type_school_encoded'] = type_school_encoded.transform([sample.type_school])[0]
    df_new_sample.loc[0, 'school_accreditation_encoded'] = school_accreditation_encoded.transform([sample.school_accreditation])[0]
    df_new_sample.loc[0, 'gender_encoded'] = gender_encoded.transform([sample.gender])[0]
    df_new_sample.loc[0, 'interest_encoded'] = interest_encoded.transform([sample.interest])
    df_new_sample.loc[0, 'residence_encoded'] = residence_encoded.transform([sample.residence])
    df_new_sample.loc[0, 'parent_was_in_college_encoded'] = parent_was_in_college_encoded.transform([sample.parent_was_in_college])

    

    return df_new_sample


def perform_prediction(sample):
    # print(f"Sample: {sample}")
    # print(sample.Parch)
    new_sample = preprocess(sample)
    print(new_sample)

    with open(CLASSIFICADOR, 'rb') as f:
        clf = pickle.load(f)

    will_go_to_college = clf.predict(new_sample)

    will_go_to_college = will_go_to_college[0]

    if will_go_to_college == True:
        wgtc_str = 'Vai para a escola.'
    else:
        wgtc_str = 'Não vai para a escola.'

    return wgtc_str
