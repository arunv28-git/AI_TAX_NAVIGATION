def detect_compliance_risk(user_inputs, regime):

    risks = []

    if regime == "New" and user_inputs.get("hra_claimed"):
        risks.append("HRA is not allowed under New Tax Regime.")

    if user_inputs.get("deductions", 0) > 150000:
        risks.append("80C deduction exceeds allowed limit (₹1.5L).")

    return risks