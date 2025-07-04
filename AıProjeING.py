import pandas as pd
import re
import streamlit as st

# Read CSV file
df = pd.read_csv("C:/Users/enesk/Desktop/Denem/DATASET.csv")
drug_names_lower = df['drug_name'].dropna().str.lower().unique()

# Functions
def is_age_appropriate(user_age, age_range_str):
    if not isinstance(age_range_str, str):
        return False
    try:
        min_age = int(re.findall(r"\d+", age_range_str)[0])
        return user_age >= min_age
    except:
        return False

def check_drug_interaction(drug1, drug2):
    row1 = df[df['drug_name'].str.lower() == drug1]
    row2 = df[df['drug_name'].str.lower() == drug2]
    if row1.empty or row2.empty:
        return "❌ At least one of the entered drugs was not found in the database."
    interactions1 = row1.iloc[0].get('drug_interactions', '').lower()
    interactions2 = row2.iloc[0].get('drug_interactions', '').lower()
    if drug2 in interactions1 or drug1 in interactions2:
        return f"⚠ There may be an interaction between {drug1} and {drug2}. Please consult your doctor."
    else:
        return "✅ There is no known issue with using these two drugs together."

# Title and session state
st.title("💬 Smart Drug Advisor Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "👋 Hello! How old are you?"}]
if "step" not in st.session_state:
    st.session_state.step = 0
if "age" not in st.session_state:
    st.session_state.age = None

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Get user input
user_message = st.chat_input("Type your message and press Enter...")

# Process input
if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})

    # Exit commands
    if user_message.lower().strip() in ["no", "exit", "quit"]:
        st.session_state.messages.append({"role": "assistant", "content": "👋 Goodbye! Stay healthy."})
        st.session_state.step = -1
        st.rerun()

    # STEP 0: Age input
    if st.session_state.step == 0:
        try:
            st.session_state.age = int(user_message)
            st.session_state.messages.append({
                "role": "assistant",
                "content": "Thanks! What would you like to do?\n1️⃣ Drug information\n2️⃣ Suggest drugs by condition\n3️⃣ Drug interaction check\n(To exit, type 'exit')"
            })
            st.session_state.step = 1
        except:
            st.session_state.messages.append({"role": "assistant", "content": "❗ Please enter a valid age (e.g., 25)."})

    # STEP 1: Menu
    elif st.session_state.step == 1:
        if user_message == "1":
            st.session_state.messages.append({"role": "assistant", "content": "📌 Which drug are you curious about?"})
            st.session_state.step = 2
        elif user_message == "2":
            st.session_state.messages.append({"role": "assistant", "content": "🩺 What condition are you dealing with? (e.g., headache)"})
            st.session_state.step = 3
        elif user_message == "3":
            st.session_state.messages.append({"role": "assistant", "content": "💊 Enter two drug names separated by a comma (e.g., aspirin, ibuprofen)"})
            st.session_state.step = 4
        else:
            st.session_state.messages.append({"role": "assistant", "content": "Please enter only 1, 2, or 3."})

    # STEP 2: Drug information
    elif st.session_state.step == 2:
        drug = user_message.lower()
        matched_row = None
        for name in drug_names_lower:
            if name in drug:
                match_df = df[df['drug_name'].str.lower() == name]
                if not match_df.empty:
                    matched_row = match_df.iloc[0]
                    break
        if matched_row is not None:
            age_range = matched_row.get("recommended_age_range", "no info")
            uygun = is_age_appropriate(st.session_state.age, age_range)
            response = f"""
            **Name:** {matched_row['drug_name']}
            **Used For:** {matched_row.get('medical_condition', 'no info')}
            **Age Suitability:** {'✅ Suitable' if uygun else '❌ Not suitable'} (Recommended age: {age_range})
            **Food Interactions:** {matched_row.get('food_interactions', 'no info')}
            **Side Effects:** {matched_row.get('side_effects', 'no info')}
            """
        else:
            response = "❌ This drug was not found in the database."
        st.session_state.messages.append({"role": "assistant", "content": response})
        # Return to menu
        st.session_state.messages.append({
            "role": "assistant",
            "content": "🔁 Want to do something else?\n1️⃣ Drug information\n2️⃣ Suggest drugs by condition\n3️⃣ Drug interaction check\n(To exit, type 'exit')"
        })
        st.session_state.step = 1

    # STEP 3: Drug recommendation by condition
    elif st.session_state.step == 3:
        condition = user_message.lower()
        matched = df[df['medical_condition'].str.lower().str.contains(condition)]
        if not matched.empty:
            drugs = matched['drug_name'].dropna().unique()
            response = "🔎 Suggested drugs:\n" + "\n".join(f"- {d}" for d in drugs)
        else:
            response = "❌ No suggestions found for this condition."
        st.session_state.messages.append({"role": "assistant", "content": response})
        # Return to menu
        st.session_state.messages.append({
            "role": "assistant",
            "content": "🔁 Want to do something else?\n1️⃣ Drug information\n2️⃣ Suggest drugs by condition\n3️⃣ Drug interaction check\n(To exit, type 'exit')"
        })
        st.session_state.step = 1

    # STEP 4: Drug interaction
    elif st.session_state.step == 4:
        drugs = [d.strip().lower() for d in user_message.split(",")]
        if len(drugs) == 2:
            result = check_drug_interaction(drugs[0], drugs[1])
        else:
            result = "⚠ Please enter only two drugs (e.g., paracetamol, ibuprofen)."
        st.session_state.messages.append({"role": "assistant", "content": result})
        # Return to menu
        st.session_state.messages.append({
            "role": "assistant",
            "content": "🔁 Want to do something else?\n1️⃣ Drug information\n2️⃣ Suggest drugs by condition\n3️⃣ Drug interaction check\n(To exit, type 'exit')"
        })
        st.session_state.step = 1

    st.rerun()

# Footer
st.markdown("---")
st.caption("⚠ This chatbot does not provide medical advice. Please consult your doctor.")
