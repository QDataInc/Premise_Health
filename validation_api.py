from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# --- Full Members Data with Validations to Test ---
members_data = [
    {"member_id": "M1001", "name": "Trevor Lowe", "email": "", "address": "9490 Dennis Circle", "ssn": "176-92-5860", "gender": "M", "dob": "1966-04-09", "join_date": "2025-06-20", "region": "California"},
    {"member_id": "M1002", "name": "Kelli Williams", "email": "kelli.williams@gmail.com", "address": "8511 Harper Ridge", "ssn": "111-65-7322", "gender": "F", "dob": "09-17-1982", "join_date": "2025-06-21", "region": "Texas"},
    {"member_id": "M1003", "name": "David Kim", "email": "david.kim@gmail.com", "address": "2489 Evans Lakes", "ssn": "645-30-5323", "gender": "M", "dob": "1976-08-02", "join_date": "2025-06-22", "region": "Texas"},
    {"member_id": "M1003", "name": "Duplicate David", "email": "david.duplicate@gmail.com", "address": "2489 Evans Lakes", "ssn": "645-30-5323", "gender": "M", "dob": "1976-08-02", "join_date": "2025-06-22", "region": "Texas"},
    {"member_id": "M1004", "name": "Lisa Green", "email": "lisa.green@gmail.com", "address": "", "ssn": "894-05-7770", "gender": "F", "dob": "1993-12-08", "join_date": "2025-06-23", "region": "Nevada"},
    {"member_id": "M1005", "name": "Ava Singh", "email": "ava.singh@gmail.com", "address": "7720 Birchwood Dr", "ssn": "000-00-0000", "gender": "F", "dob": "wrongformat", "join_date": "2025-06-24", "region": "Florida"},
]

# --- Full Claims Data with Validations to Test ---
claims_data = [
    {"claim_id": "", "member_id": "M1001", "service_start_date": "2025-06-21", "service_end_date": "2025-06-23", "diagnosis": "Diabetes", "provider_id": "PR200", "procedure": "CPT 94010", "amount_billed": 12000.00},
    {"claim_id": "C3002", "member_id": "M1001", "service_start_date": "2025-06-24", "service_end_date": "2025-06-26", "diagnosis": "Diabetes", "provider_id": "PR210", "procedure": "CPT 94010", "amount_billed": 195.63},
    {"claim_id": "C3003", "member_id": "M1001", "service_start_date": "2025-06-24", "service_end_date": "2025-06-26", "diagnosis": "Diabetes", "provider_id": "PR210", "procedure": "CPT 94010", "amount_billed": 195.63},
    {"claim_id": "C3004", "member_id": "M1002", "service_start_date": "2026-01-01", "service_end_date": "2026-01-03", "diagnosis": "Migraine", "provider_id": "PR206", "procedure": "CPT 99213", "amount_billed": 594.13},
    {"claim_id": "C3005", "member_id": "M1003", "service_start_date": "2025-07-01", "service_end_date": "2025-07-03", "diagnosis": "Back Pain", "provider_id": "PR208", "procedure": "CPT 97110", "amount_billed": None},
    {"claim_id": "C3006", "member_id": "M1004", "service_start_date": "wrong-date", "service_end_date": "2025-07-10", "diagnosis": "Hypertension", "provider_id": "PR309", "procedure": "CPT 96372", "amount_billed": 400.00}
]

# --- New API to return full members dataset ---
@app.route('/membersdata', methods=['GET'])
def get_all_members():
    return jsonify(members_data)

# --- New API to return full claims dataset ---
@app.route('/claimsdata', methods=['GET'])
def get_all_claims():
    return jsonify(claims_data)

# --- Run the Flask app ---
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
