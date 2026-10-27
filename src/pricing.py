RATES = {
    "regular": 6000,
    "express": 10000,
}

def calculate_laundry_cost(weight_kg, service_type):
    if not isinstance(weight_kg, (int, float)) or isinstance(weight_kg, bool):
        raise TypeError("Berat harus berupa angka numerik!")
    if weight_kg <= 0:
        raise ValueError("Berat cucian harus lebih berat dari 0!")

    clean_service = service_type.strip().lower()
    if clean_service not in RATES:
        raise ValueError("Jenis layanan tidak valid!")

    # Aturan batas minimum 1.0kg
    billable_weight = max (1.0, float(weight_kg))

    total = billable_weight * RATES[clean_service]
    return int(total)