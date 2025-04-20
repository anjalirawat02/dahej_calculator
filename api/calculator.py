def calculate_dahej(data):
    name = data.get("name")
    age = int(data.get("age", 0))
    face_color = data.get("face_color")
    land_own = float(data.get("land_own", 0))
    land_father = float(data.get("land_father", 0))
    earning_own = float(data.get("earning_own", 0))
    earning_father = float(data.get("earning_father", 0))
    father_status = data.get("father_status")
    brothers = int(data.get("brothers", 0))
    sisters = int(data.get("sisters", 0))
    home_ownership = data.get("home_ownership")
    home_location = data.get("home_location")

    # Required field check
    required_fields = [name, face_color, father_status, home_ownership, home_location]
    if any(field is None or str(field).strip() == "" for field in required_fields):
        return "All required fields must be filled!"

    dahej = 1000000  # base value (₹10 lakh base)

    # Age factor (modifying weight to make age factor less dominant)
    if 20 <= age <= 30:
        dahej += 200000  # adding 3 lakh for age between 20-30
    elif 30 < age <= 40:
        dahej += 100000  # adding 1.5 lakh for age between 30-40
    else:
        dahej += 10000   # adding 50k for older than 40

    # Face complexion (considering this factor remains consistent but not too high)
    if face_color == "Bright":
        dahej += 50000  # adding 50k for bright complexion
    elif face_color == "Medium":
        dahej += 10000   # adding 10k for fair complexion
    else:
        dahej += 1000   # adding 1k for dusky complexion

    # Land (reducing weight to prevent too much contribution)
    dahej += (land_own + land_father) * 10000  # 10k for each acre of land owned

    # Income (increase the weight of own income)
    dahej += earning_own * 24  # 2 years of own salary (own income gives higher weight)
    dahej += earning_father * 4  # 4 months of father's salary (less weight for father’s income)

    # Father's earning status
    if father_status == "Earning":
        dahej += 10000
    elif father_status == "Retired":
        dahej += 5000

    # Family size factor (modifying these factors to ensure they don't make too much difference)
    dahej -= brothers * 20000   # 20k for each brother
    dahej -= sisters * 5000     # 5k deduction for each sister

    # Home ownership (adding a reasonable amount for owning a home)
    if home_ownership == "Own":
        dahej += 200000  # 2 lakh for owning a home
    else:
        dahej += 10000   # 10k for renting a home

    # Home location (urban vs rural adjustment)
    if home_location == "Urban":
        dahej += 100000  # 1 lakh for urban location
    else:
        dahej += 50000   # 50k for rural location

    # Returning the final calculated dahej as an integer value
    return int(dahej)
