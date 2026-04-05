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