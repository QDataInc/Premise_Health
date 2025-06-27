from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Simulated data
claims_data = [
    {
        "claim_id": "C1001", "patient_name": "John Smith", "ssn": "123-45-6789",
        "dob": "1980-05-15", "gender": "M", "diagnosis": "Diabetes Type 2",
        "procedure": "CPT 82947", "provider_id": "PR200", "amount_billed": 235.00,
        "last_modified": "2025-06-24T10:00:00Z"
    },
    {
        "claim_id": "C1002", "patient_name": "Alice Jones", "ssn": "456-78-9012",
        "dob": "1975-09-02", "gender": "F", "diagnosis": "Hypertension",
        "procedure": "CPT 99213", "provider_id": "PR201", "amount_billed": 150.00,
        "last_modified": "2025-06-25T12:30:00Z"
    },
    {
        "claim_id": "C1003", "patient_name": "Robert Lee", "ssn": "789-01-2345",
        "dob": "1992-12-22", "gender": "M", "diagnosis": "Asthma",
        "procedure": "CPT 94010", "provider_id": "PR202", "amount_billed": 180.00,
        "last_modified": "2025-06-25T14:15:00Z"
    },
    {
        "claim_id": "C1004", "patient_name": "Mary Evans", "ssn": "234-56-7890",
        "dob": "1986-07-11", "gender": "F", "diagnosis": "Fracture Arm",
        "procedure": "CPT 24500", "provider_id": "PR203", "amount_billed": 1200.00,
        "last_modified": "2025-06-25T15:20:00Z"
    },
    {
        "claim_id": "C1005", "patient_name": "David Kim", "ssn": "345-67-8901",
        "dob": "1990-11-05", "gender": "M", "diagnosis": "Migraine",
        "procedure": "CPT 96372", "provider_id": "PR204", "amount_billed": 220.00,
        "last_modified": "2025-06-24T09:45:00Z"
    },
    {
        "claim_id": "C1006", "patient_name": "Lisa Green", "ssn": "567-89-0123",
        "dob": "1988-03-18", "gender": "F", "diagnosis": "Anxiety",
        "procedure": "CPT 96127", "provider_id": "PR205", "amount_billed": 175.00,
        "last_modified": "2025-06-26T08:00:00Z"
    },
    {
        "claim_id": "C1007", "patient_name": "James Young", "ssn": "890-12-3456",
        "dob": "1982-10-29", "gender": "M", "diagnosis": "High Cholesterol",
        "procedure": "CPT 80061", "provider_id": "PR206", "amount_billed": 140.00,
        "last_modified": "2025-06-26T08:15:00Z"
    },
    {
        "claim_id": "C1008", "patient_name": "Nancy Drew", "ssn": "678-90-1234",
        "dob": "1995-01-14", "gender": "F", "diagnosis": "Depression",
        "procedure": "CPT 90834", "provider_id": "PR207", "amount_billed": 300.00,
        "last_modified": "2025-06-26T09:30:00Z"
    },
    {
        "claim_id": "C1009", "patient_name": "Mark Allen", "ssn": "901-23-4567",
        "dob": "1970-06-09", "gender": "M", "diagnosis": "Back Pain",
        "procedure": "CPT 97110", "provider_id": "PR208", "amount_billed": 400.00,
        "last_modified": "2025-06-25T11:10:00Z"
    },
    {
        "claim_id": "C1010", "patient_name": "Susan White", "ssn": "012-34-5678",
        "dob": "1984-08-21", "gender": "F", "diagnosis": "Insomnia",
        "procedure": "CPT 95810", "provider_id": "PR209", "amount_billed": 600.00,
        "last_modified": "2025-06-26T10:00:00Z"
    }
]

@app.route('/claims', methods=['GET'])
def get_claims():
    since = request.args.get('since', None)
    if since:
        try:
            since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))
            filtered = [c for c in claims_data if datetime.fromisoformat(c["last_modified"].replace("Z", "+00:00")) > since_dt]
            return jsonify(filtered)
        except ValueError:
            return jsonify({"error": "Invalid date format. Use ISO 8601."}), 400
    return jsonify(claims_data)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Needed for Render
    app.run(host="0.0.0.0", port=port)