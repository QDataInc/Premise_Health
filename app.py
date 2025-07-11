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











# from flask import Flask, jsonify, request
# from datetime import datetime

# app = Flask(__name__)

# members_data = [
#     {"member_id": "M1001", "name": "Trevor Lowe", "email": "trevor.lowe@gmail.com", "address": "9490 Dennis Circle", "ssn": "176-92-5860", "gender": "M", "dob": "1966-04-09", "join_date": "2025-06-20"},
#     {"member_id": "M1002", "name": "Kelli Williams", "email": "kelli.williams@gmail.com", "address": "8511 Harper Ridge", "ssn": "111-65-7322", "gender": "F", "dob": "1982-09-17", "join_date": "2025-06-21"},
#     {"member_id": "M1003", "name": "David Kim", "email": "david.kim@gmail.com", "address": "2489 Evans Lakes", "ssn": "645-30-5323", "gender": "M", "dob": "1976-08-02", "join_date": "2025-06-22"},
#     {"member_id": "M1004", "name": "Lisa Green", "email": "lisa.green@gmail.com", "address": "83191 Kevin Parkway", "ssn": "894-05-7770", "gender": "F", "dob": "1993-12-08", "join_date": "2025-06-23"},
#     {"member_id": "M1005", "name": "James Young", "email": "james.young@gmail.com", "address": "8692 Andrew Locks", "ssn": "283-52-5160", "gender": "M", "dob": "1964-12-30", "join_date": "2025-06-24"},
#     {"member_id": "M1006", "name": "Sophia Turner", "email": "sophia.turner@gmail.com", "address": "7720 Maple Crest Blvd", "ssn": "349-88-9131", "gender": "F", "dob": "1989-03-25", "join_date": "2025-06-25"},
#     {"member_id": "M1007", "name": "Ethan Brooks", "email": "ethan.brooks@gmail.com", "address": "6612 Willow Oak Dr", "ssn": "527-41-6203", "gender": "M", "dob": "1975-06-11", "join_date": "2025-06-26"},
#     {"member_id": "M1008", "name": "Ava Patel", "email": "ava.patel@gmail.com", "address": "5821 Kingston Cove", "ssn": "408-39-2624", "gender": "F", "dob": "1991-01-05", "join_date": "2025-06-27"},
#     {"member_id": "M1009", "name": "Liam Johnson", "email": "liam.johnson@gmail.com", "address": "9003 Whispering Way", "ssn": "266-58-1930", "gender": "M", "dob": "1984-11-13", "join_date": "2025-06-28"},
#     {"member_id": "M1010", "name": "Chloe Ramirez", "email": "chloe.ramirez@gmail.com", "address": "4417 Summit Lane", "ssn": "362-92-8460", "gender": "F", "dob": "1997-07-21", "join_date": "2025-06-29"},
# ]


# # members_data = [
# #     {"member_id": "M1001", "name": "Trevor Lowe", "email": "trevor.lowe@gmail.com", "address": "9490 Dennis Circle", "ssn": "176-92-5860", "gender": "M", "dob": "1966-04-09", "join_date": "2025-06-20"},
# #     {"member_id": "M1002", "name": "Kelli Williams", "email": "kelli.williams@gmail.com", "address": "8511 Harper Ridge", "ssn": "111-65-7322", "gender": "F", "dob": "1982-09-17", "join_date": "2025-06-21"},
# #     {"member_id": "M1003", "name": "David Kim", "email": "david.kim@gmail.com", "address": "2489 Evans Lakes", "ssn": "645-30-5323", "gender": "M", "dob": "1976-08-02", "join_date": "2025-06-22"},
# #     {"member_id": "M1004", "name": "Lisa Green", "email": "lisa.green@gmail.com", "address": "83191 Kevin Parkway", "ssn": "894-05-7770", "gender": "F", "dob": "1993-12-08", "join_date": "2025-06-23"},
# #     {"member_id": "M1005", "name": "James Young", "email": "james.young@gmail.com", "address": "8692 Andrew Locks", "ssn": "283-52-5160", "gender": "M", "dob": "1964-12-30", "join_date": "2025-06-24"},
# # ]

# claims_data = [
#     {"claim_id": "C2001", "member_id": "M1001", "service_start_date": "2025-06-21", "service_end_date": "2025-06-23", "diagnosis": "Diabetes", "provider_id": "PR200", "procedure": "CPT 94010", "amount_billed": 369.38},
#     {"claim_id": "C2002", "member_id": "M1001", "service_start_date": "2025-06-24", "service_end_date": "2025-06-26", "diagnosis": "Diabetes", "provider_id": "PR210", "procedure": "CPT 96372", "amount_billed": 195.63},
#     {"claim_id": "C2003", "member_id": "M1001", "service_start_date": "2025-06-27", "service_end_date": "2025-06-29", "diagnosis": "Diabetes", "provider_id": "PR200", "procedure": "CPT 82947", "amount_billed": 340.50},
#     {"claim_id": "C2004", "member_id": "M1002", "service_start_date": "2025-07-01", "service_end_date": "2025-07-03", "diagnosis": "Migraine", "provider_id": "PR200", "procedure": "CPT 96372", "amount_billed": 318.72},
#     {"claim_id": "C2005", "member_id": "M1002", "service_start_date": "2025-07-05", "service_end_date": "2025-07-08", "diagnosis": "Migraine", "provider_id": "PR206", "procedure": "CPT 99213", "amount_billed": 594.13},
#     {"claim_id": "C2006", "member_id": "M1003", "service_start_date": "2025-07-10", "service_end_date": "2025-07-11", "diagnosis": "Back Pain", "provider_id": "PR208", "procedure": "CPT 97110", "amount_billed": 400.00},
#     {"claim_id": "C2007", "member_id": "M1003", "service_start_date": "2025-07-13", "service_end_date": "2025-07-14", "diagnosis": "Back Pain", "provider_id": "PR208", "procedure": "CPT 97110", "amount_billed": 400.00},
#     {"claim_id": "C2008", "member_id": "M1004", "service_start_date": "2025-07-16", "service_end_date": "2025-07-17", "diagnosis": "Hypertension", "provider_id": "PR309", "procedure": "CPT 96372", "amount_billed": 400.00},
#     {"claim_id": "C2009", "member_id": "M1004", "service_start_date": "2025-07-19", "service_end_date": "2025-07-21", "diagnosis": "Hypertension", "provider_id": "PR309", "procedure": "CPT 96372", "amount_billed": 400.00},
#     {"claim_id": "C2010", "member_id": "M1004", "service_start_date": "2025-07-23", "service_end_date": "2025-07-25", "diagnosis": "Hypertension", "provider_id": "PR309", "procedure": "CPT 96372", "amount_billed": 400.00},
# ]

# # GET /members?date_gt=2025-06-23&date_lt=2025-06-26
# @app.route('/members', methods=['GET'])
# def get_members():
#     gt_date = request.args.get('date_gt')
#     lt_date = request.args.get('date_lt')
#     result = members_data

#     try:
#         if gt_date:
#             gt_dt = datetime.strptime(gt_date, "%Y-%m-%d")
#             result = [m for m in result if datetime.strptime(m["join_date"], "%Y-%m-%d") > gt_dt]

#         if lt_date:
#             lt_dt = datetime.strptime(lt_date, "%Y-%m-%d")
#             result = [m for m in result if datetime.strptime(m["join_date"], "%Y-%m-%d") < lt_dt]

#     except ValueError:
#         return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

#     return jsonify(result)

# # GET /claims?date_gt=2025-06-23&date_lt=2025-06-26
# @app.route('/claims', methods=['GET'])
# def get_claims():
#     gt_date = request.args.get('date_gt')
#     lt_date = request.args.get('date_lt')
#     result = claims_data

#     try:
#         if gt_date:
#             gt_dt = datetime.strptime(gt_date, "%Y-%m-%d")
#             result = [c for c in result if datetime.strptime(c["service_start_date"], "%Y-%m-%d") > gt_dt]

#         if lt_date:
#             lt_dt = datetime.strptime(lt_date, "%Y-%m-%d")
#             result = [c for c in result if datetime.strptime(c["service_start_date"], "%Y-%m-%d") < lt_dt]

#     except ValueError:
#         return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

#     return jsonify(result)

# if __name__ == '__main__':
#     import os
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)