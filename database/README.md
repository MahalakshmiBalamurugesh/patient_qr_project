Database Design

Tables:
- patients: stores patient info and login (ID, PIN)
- doctors: stores doctor info
- medical_records: stores medical history
- qr_codes: links QR to patient
- access_requests: controls access permission

Flow:
1. Patient registers
2. QR is generated
3. Doctor scans QR
4. Patient approves request
5. Doctor accesses data
6. Doctor adds new records

QR Access Flow:

1. Patient QR contains a unique token
2. Doctor scans QR
3. System identifies patient using QR
4. Access request is created (status = pending)
5. Patient can approve or reject
6. If approved → doctor can view medical records

Doctor Medical Record Flow:

1. Doctor scans QR and requests access
2. Patient approves access
3. Doctor can view existing medical records
4. Doctor can add new records
5. Each record is stored with patient_id and doctor_id