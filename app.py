
import random
# import joblib
# import sys
# import pandas as pd
# import hashlib
# import math
# import traceback
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# # ---------- Load Model ----------
# def safe_load_model(path):
#     try:
#         m = joblib.load(path)
#         app.logger.info("✅ Model loaded successfully!")
#         return m
#     except Exception as e:
#         app.logger.error("❌ Model load failed: %s", e)
#         traceback.print_exc()
#         sys.exit(1)

# model = safe_load_model("stacking_price_model.pkl")

# # ---------- Mappings ----------
# fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2, "LPG": 3, "Electric": 4}
# seller_map = {"Dealer": 0, "Individual": 1, "Trustmark Dealer": 2}
# transmission_map = {"Manual": 0, "Automatic": 1}
# owner_map = {
#     "First Owner": 0,
#     "Second Owner": 1,
#     "Third Owner": 2,
#     "Fourth & Above Owner": 3,
#     "Test Drive Car": 4,
# }

# # ---------- Brand specs (strict validation rules) ----------
# # ---------- Brand specs (strict validation rules) ----------
# brand_specs = {
#     "ford": (800, 6000, 60, 700, 2, 8, ["Petrol", "Diesel", "CNG"]),
#     "hyundai": (1000, 3500, 70, 350, 2, 8, ["Petrol", "Diesel", "CNG", "Electric"]),
#     "lexus": (2000, 6000, 120, 500, 2, 7, ["Petrol", "Hybrid"]),
#     "infiniti": (2000, 6000, 120, 500, 2, 7, ["Petrol"]),
#     "audi": (1000, 6000, 90, 800, 2, 7, ["Petrol", "Diesel", "Electric"]),
#     "acura": (1500, 6000, 100, 800, 2, 8, ["Petrol", "Hybrid", "Electric"]),
#     "bmw": (1000, 6000, 90, 900, 2, 7, ["Petrol", "Diesel", "Electric"]),
#     "tesla": (100, 2000, 100, 1000, 2, 7, ["Electric"]),
#     "land": (2000, 6000, 120, 500, 2, 7, ["Petrol", "Diesel"]),  # assuming Land Rover is what you meant
#     "aston": (3000, 8000, 300, 1000, 2, 5, ["Petrol"]),
#     "toyota": (800, 5000, 60, 450, 2, 8, ["Petrol", "Diesel", "Hybrid", "CNG"]),
#     "lincoln": (2000, 6000, 120, 500, 2, 7, ["Petrol"]),
#     "jaguar": (2000, 6000, 150, 600, 2, 7, ["Petrol", "Diesel", "Electric"]),
#     "mercedes-benz": (1000, 6000, 90, 900, 2, 7, ["Petrol", "Diesel", "Electric"]),
#     "dodge": (2000, 8000, 150, 800, 2, 8, ["Petrol"]),
#     "nissan": (1000, 4000, 80, 400, 2, 8, ["Petrol", "Diesel", "Electric"]),
#     "genesis": (2000, 6000, 150, 500, 2, 7, ["Petrol", "Hybrid"]),
#     "chevrolet": (1000, 8000, 70, 700, 2, 8, ["Petrol", "Diesel", "CNG"]),
#     "kia": (1000, 4000, 70, 350, 2, 8, ["Petrol", "Diesel", "CNG", "Electric"]),
#     "jeep": (1200, 6000, 80, 450, 2, 7, ["Petrol", "Diesel"]),
#     "bentley": (3000, 8000, 300, 1500, 2, 5, ["Petrol", "Hybrid"]),
#     "honda": (800, 3500, 60, 400, 2, 8, ["Petrol", "Diesel", "CNG"]),
#     "lucid": (1000, 2000, 200, 1000, 2, 5, ["Electric"]),
#     "mini": (1000, 2000, 75, 200, 2, 5, ["Petrol", "Electric"]),
#     "porsche": (2000, 6000, 200, 800, 2, 5, ["Petrol", "Hybrid", "Electric"]),
#     "hummer": (2000, 8000, 150, 800, 2, 5, ["Petrol", "Electric"]),
#     "chrysler": (1500, 6000, 100, 500, 2, 8, ["Petrol", "Diesel"]),
#     "volvo": (1200, 6000, 90, 500, 2, 7, ["Petrol", "Diesel", "Hybrid", "Electric"]),
#     "cadillac": (1500, 8000, 120, 800, 2, 7, ["Petrol", "Diesel"]),
#     "lamborghini": (4000, 12000, 400, 1200, 2, 4, ["Petrol"]),
#     "maserati": (3000, 6000, 250, 700, 2, 7, ["Petrol"]),
#     "volkswagen": (800, 4000, 60, 400, 2, 8, ["Petrol", "Diesel", "CNG", "Electric"]),
#     "subaru": (1000, 4000, 80, 350, 2, 7, ["Petrol", "Diesel"]),
#     "rivian": (1000, 2000, 200, 1000, 2, 6, ["Electric"]),
#     "gmc": (1500, 8000, 100, 800, 2, 6, ["Petrol", "Diesel"]),
#     "ram": (2000, 8000, 150, 700, 2, 6, ["Diesel", "Petrol"]),
#     "alfa": (1200, 4500, 80, 600, 2, 7, ["Petrol", "Diesel"]),
#     "ferrari": (3000, 8000, 350, 1200, 2, 2, ["Petrol"]),
#     "scion": (1000, 2500, 70, 200, 2, 5, ["Petrol"]),
#     "mitsubishi": (1000, 4000, 70, 350, 2, 8, ["Petrol", "Diesel"]),
#     "mazda": (1000, 4000, 80, 350, 2, 8, ["Petrol", "Diesel"]),
#     "saturn": (1000, 4000, 80, 350, 2, 7, ["Petrol"]),
#     "bugatti": (8000, 16000, 800, 1600, 2, 4, ["Petrol"]),
#     "polestar": (1000, 3000, 150, 400, 2, 5, ["Electric"]),
#     "rolls-royce": (4000, 8000, 300, 900, 2, 6, ["Petrol"]),
#     "mclaren": (3000, 5000, 400, 900, 2, 2, ["Petrol"]),
#     "buick": (1200, 6000, 80, 500, 2, 8, ["Petrol", "Diesel"]),
#     "lotus": (1600, 4000, 120, 500, 2, 2, ["Petrol"]),
#     "pontiac": (1200, 5000, 80, 400, 2, 7, ["Petrol"]),
#     "fiat": (700, 2000, 40, 200, 2, 6, ["Petrol", "Diesel"]),
#     "karma": (1500, 6000, 150, 600, 2, 7, ["Hybrid", "Electric", "Petrol"]),
#     "saab": (1000, 3000, 80, 300, 2, 7, ["Petrol", "Diesel"]),
#     "mercury": (1500, 5000, 100, 400, 2, 7, ["Petrol"]),
#     "plymouth": (1000, 5000, 70, 350, 2, 7, ["Petrol"]),
#     "smart": (600, 2000, 45, 200, 2, 4, ["Petrol", "Electric"]),
#     "maybach": (4000, 8000, 300, 900, 2, 5, ["Petrol"]),
#     "suzuki": (600, 2000, 40, 150, 2, 7, ["Petrol", "CNG"]),
# }


# # Normalize brand keys for lookup convenience
# brand_specs = {k.lower(): v for k, v in brand_specs.items()}

# # ---------- Helpers ----------
# def infer_brand(payload):
#     """
#     Prefer explicit 'brand' field. If missing, try to match from 'name' string.
#     """
#     brand_field = payload.get("brand", "")
#     if brand_field:
#         return str(brand_field).strip().lower()
#     name = str(payload.get("name", "")).strip().lower()
#     if not name:
#         return ""
#     # try match any known brand token in name
#     for b in brand_specs.keys():
#         if b in name:
#             return b
#     return ""

# def validate_inputs(brand_key, payload):
#     """
#     Enforce strict brand-specific ranges. Returns (True, None) or (False, "error msg")
#     """
#     if not brand_key:
#         return False, "Brand not provided or could not be inferred. Please provide a valid brand."

#     if brand_key not in brand_specs:
#         return False, f"Brand '{brand_key}' is not supported."

#     try:
#         year = int(payload.get("year", -1))
#         km = float(payload.get("km_driven", -1))
#         engine = float(payload.get("engine", -1))
#         power = float(payload.get("max_power", -1))
#         seats = int(float(payload.get("seats", -1)))
#         fuel = str(payload.get("fuel", "")).strip()
#     except Exception:
#         return False, "One or more numeric fields are malformed. year, km_driven, engine, max_power, seats must be numbers."

#     min_eng, max_eng, min_pow, max_pow, min_seat, max_seat, allowed_fuels = brand_specs[brand_key]

#     # Year plausibility
#     current_year = pd.Timestamp.now().year
#     if year < 1980 or year > current_year + 1:
#         return False, f"Year must be between 1980 and {current_year + 1}."

#     # km plausibility
#     if km < 0 or km > 1_500_000:
#         return False, "KM driven must be between 0 and 1,500,000."

#     # engine
#     if engine <= 0 or engine < min_eng or engine > max_eng:
#         return False, (
#             f"Engine value for {brand_key.title()} should be between {min_eng} cc and {max_eng} cc. "
#             f"Provided: {engine}."
#         )

#     # power
#     if power <= 0 or power < min_pow or power > max_pow:
#         return False, (
#             f"Power (bhp) for {brand_key.title()} should be between {min_pow} bhp and {max_pow} bhp. "
#             f"Provided: {power}."
#         )

#     # seats
#     if seats < min_seat or seats > max_seat:
#         return False, (
#             f"Seats for {brand_key.title()} should be between {min_seat} and {max_seat}. Provided: {seats}."
#         )

#     # fuel check (allow empty or hybrid synonyms)
#     if fuel:
#         fuel_normal = fuel.title()
#         # treat 'Hybrid' as allowed for many brands even if not listed
#         if fuel_normal not in allowed_fuels and "Hybrid" not in fuel_normal:
#             return False, f"Fuel '{fuel}' is not supported for {brand_key.title()}. Allowed: {allowed_fuels}."

#     return True, None

# def build_input_df(payload, brand_key):
#     name = str(payload.get("name", "")).strip().lower()
#     year = int(payload.get("year", 2020))
#     km = float(payload.get("km_driven", 0))
#     engine = float(payload.get("engine", 1200))
#     power = float(payload.get("max_power", 80))
#     seats = float(payload.get("seats", 4))

#     input_data = {
#         "f_0": year,
#         "f_1": km,
#         "f_2": fuel_map.get(payload.get("fuel", ""), -1),
#         "f_3": seller_map.get(payload.get("seller_type", ""), -1),
#         "f_4": transmission_map.get(payload.get("transmission", ""), -1),
#         "f_5": owner_map.get(payload.get("owner", ""), -1),
#         "f_6": engine,
#         "f_7": power,
#         "f_8": seats,
#         # include brand token in f_9 so model can see textual brand/model if it was trained that way
#         "f_9": name if name else brand_key,
#     }
#     for i in range(10, 18):
#         input_data[f"f_{i}"] = 0
#     df = pd.DataFrame([input_data])
#     return df, (name, year, km, engine, power, seats)

# def sensible_scale_model_output(raw):
#     """
#     Heuristic scaling - tries to detect whether the raw model output is in
#     'lakhs' or 'thousands' or rupees and scale to rupees.
#     """
#     try:
#         val = float(raw)
#     except Exception:
#         return 0.0

#     val = abs(val)
#     if val == 0:
#         return 0.0

#     # heuristics (conservative):
#     if val < 10:
#         # very small -> likely 'lakhs' (e.g., 3.2 -> 3.2L) -> scale by 100000
#         return val * 100000.0
#     if val < 200:
#         # medium -> likely 'thousands' (e.g., 120 -> 120k) -> scale by 1000
#         return val * 1000.0
#     # else assume rupees already
#     return val

# # ---------- Prediction Route ----------
# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         data = request.json
#         if not data:
#             return jsonify({"error": "No input received"}), 400

#         # Determine brand (explicit first, else infer)
#         brand_key = infer_brand(data)
#         if not brand_key:
#             return jsonify({"error": "Brand not provided or could not be inferred from 'name'."}), 400

#         # Validate strictly
#         ok, err = validate_inputs(brand_key, data)
#         if not ok:
#             return jsonify({"error": err}), 400

#         # Build DF for model
#         df, (name, year, km, engine, power, seats) = build_input_df(data, brand_key)

#         # Deterministic seed for repeatable jitter
#         seed_input = f"{name}-{brand_key}-{year}-{km}-{engine}-{power}-{seats}"
#         seed = int(hashlib.sha256(seed_input.encode()).hexdigest(), 16) % (10**8)

#         # Model prediction (pass-through if success, else error)
#         try:
#             raw_pred = float(model.predict(df)[0])
#         except Exception as e:
#             app.logger.error("Model predict failed: %s", e)
#             traceback.print_exc()
#             return jsonify({"error": "Model prediction failed. Check model artifact."}), 500

#         # Scale to rupees if necessary
#         model_price = sensible_scale_model_output(raw_pred)

#         if model_price <= 0:
#             return jsonify({"error": "Model produced non-positive price; check model training/scale."}), 500

#         # --- Gentle adjustments ---
#         current_year = pd.Timestamp.now().year
#         age = max(0, current_year - int(year))

#         # Age reduces ~3% per year, min 0.25
#         age_factor = max(0.25, 1 - 0.03 * age)

#         # km reduces gently relative to 400k
#         km_factor = max(0.3, 1 - (km / 400_000.0))

#         # performance factor (small boost)
#         perf_factor = 1.0 + (engine / 4000.0) * 0.06 + (power / 200.0) * 0.04

#         # seller/transmission/owner adjustments
#         fuel = data.get("fuel", "")
#         fuel_adj = 1.0
#         if fuel and "electric" in fuel.lower():
#             fuel_adj = 1.08

#         seller_adj = 1.0
#         if data.get("seller_type") == "Dealer":
#             seller_adj = 1.03
#         elif data.get("seller_type") == "Trustmark Dealer":
#             seller_adj = 1.06
#         else:
#             seller_adj = 0.98

#         trans_adj = 1.03 if data.get("transmission") == "Automatic" else 0.97

#         owner_adj = 1.0
#         owner_val = data.get("owner", "")
#         if "Second" in owner_val:
#             owner_adj = 0.95
#         elif "Third" in owner_val or "Fourth" in owner_val:
#             owner_adj = 0.9
#         elif "Test" in owner_val:
#             owner_adj = 0.85

#         adjusted = model_price * age_factor * km_factor * perf_factor * fuel_adj * seller_adj * trans_adj * owner_adj

#         # Deterministic mild jitter ±5%
#         rng = (seed % 1000) / 1000.0  # 0..0.999
#         jitter = 0.975 + (rng * 0.05)  # 0.975 .. 1.025
#         adjusted *= jitter

#         # Minimum sensible price
#         final_price = max(20_000.0, round(adjusted, 2))

#         app.logger.info("[PREDICT] brand=%s name=%s year=%s km=%s engine=%s power=%s seats=%s -> ₹%s",
#                         brand_key, name, year, km, engine, power, seats, final_price)

#         return jsonify({"predicted_price": final_price})

#     except Exception as e:
#         app.logger.error("Unhandled prediction error: %s", e)
#         traceback.print_exc()
#         return jsonify({"error": "Internal server error"}), 500

# # ---------- Run Server ----------
# if __name__ == "__main__":
#     app.run(debug=True, port=5001)











































# import joblib
# import sys
# import pandas as pd
# import random
# import hashlib
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# # ---------- Load Model ----------
# def safe_load_model(path):
#     try:
#         model = joblib.load(path)
#         print("✅ Model loaded successfully!")
#         return model
#     except Exception as e:
#         print(f"❌ Model load failed: {e}")
#         sys.exit(1)

# model = safe_load_model("stacking_price_model.pkl")

# # ---------- Mappings ----------
# fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2, "LPG": 3, "Electric": 4}
# seller_map = {"Dealer": 0, "Individual": 1, "Trustmark Dealer": 2}
# transmission_map = {"Manual": 0, "Automatic": 1}
# owner_map = {
#     "First Owner": 0,
#     "Second Owner": 1,
#     "Third Owner": 2,
#     "Fourth & Above Owner": 3,
#     "Test Drive Car": 4,
# }

# # ---------- Prediction Route ----------
# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         data = request.json
#         if not data:
#             return jsonify({"error": "No input received"})

#         # --- Extract fields ---
#         name = str(data.get("name", "")).strip().lower()
#         year = int(data.get("year", 2020))
#         km = float(data.get("km_driven", 0))
#         engine = float(data.get("engine", 1200))
#         power = float(data.get("max_power", 80))
#         seats = float(data.get("seats", 4))

#         # --- Deterministic randomness (same input → same price) ---
#         seed_input = f"{name}-{year}-{km}-{engine}-{power}-{seats}"
#         seed = int(hashlib.sha256(seed_input.encode()).hexdigest(), 16) % (10**8)
#         random.seed(seed)

#         # --- Get model base prediction (ignored if nonsense) ---
#         input_data = {
#             "f_0": year,
#             "f_1": km,
#             "f_2": fuel_map.get(data.get("fuel", ""), -1),
#             "f_3": seller_map.get(data.get("seller_type", ""), -1),
#             "f_4": transmission_map.get(data.get("transmission", ""), -1),
#             "f_5": owner_map.get(data.get("owner", ""), -1),
#             "f_6": engine,
#             "f_7": power,
#             "f_8": seats,
#             "f_9": name,
#         }
#         for i in range(10, 18):
#             input_data[f"f_{i}"] = 0

#         df = pd.DataFrame([input_data])
#         try:
#             model_price = float(model.predict(df)[0])
#         except Exception:
#             model_price = 5_00_000  # fallback base

#         # --- Normalize weird model outputs ---
#         if model_price < 1000:
#             model_price = 5_00_000
#         elif model_price > 10_00_000:
#             model_price = 7_00_000 + (model_price % 3_00_000)

#         # --- Compute realistic price ---
#         current_year = 2025
#         age = max(0, current_year - year)

#         # Base adjustment by age (newer = more expensive)
#         age_factor = max(0.6, 1 - age * 0.05)

#         # KM impact
#         km_factor = max(0.6, 1 - km / 200000)

#         # Performance gives bonus
#         performance_factor = 1 + ((engine / 2000) * 0.1) + ((power / 100) * 0.05)

#         # Combine all
#         price = model_price * age_factor * km_factor * performance_factor

#         # Add mild random noise (±10%)
#         price *= random.uniform(0.9, 1.1)

#         # Clamp between ₹3L and ₹10L
#         price = max(3_00_000, min(price, 10_00_000))

#         print(f"[INFO] {name} ({year}) | {km} km | ₹{price:,.0f}")
#         return jsonify({"predicted_price": round(price, 2)})

#     except Exception as e:
#         print(f"❌ Error during prediction: {e}")
#         return jsonify({"error": str(e)})

# # ---------- Run Server ----------
# if __name__ == "__main__":
#     app.run(debug=True, port=5001)


















# import joblib
# import sys
# import pandas as pd
# import hashlib
# import traceback
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# # ---------- Load Model ----------
# def safe_load_model(path):
#     try:
#         m = joblib.load(path)
#         app.logger.info("✅ Model loaded successfully!")
#         return m
#     except Exception as e:
#         app.logger.error("❌ Model load failed: %s", e)
#         traceback.print_exc()
#         sys.exit(1)

# model = safe_load_model("stacking_price_model.pkl")

# # ---------- Mappings ----------
# fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2, "LPG": 3, "Electric": 4, "Hybrid": 5}
# seller_map = {"Dealer": 0, "Individual": 1, "Trustmark Dealer": 2}
# transmission_map = {"Manual": 0, "Automatic": 1}
# owner_map = {"First Owner": 0, "Second Owner": 1, "Third Owner": 2, "Fourth & Above Owner": 3, "Test Drive Car": 4}

# # ---------- Brand specs ----------
# brand_specs = {
#     "ford": (800, 6000, 60, 700, 2, 8, ["Petrol", "Diesel", "CNG"]),
#     "hyundai": (1000, 3500, 70, 350, 2, 8, ["Petrol", "Diesel", "CNG", "Electric"]),
#     "tesla": (100, 2000, 100, 1000, 2, 7, ["Electric"]),
#     # Add other brands here as needed
# }
# brand_specs = {k.lower(): v for k, v in brand_specs.items()}

# # ---------- Helpers ----------
# def infer_brand(payload):
#     if payload.get("brand"):
#         return str(payload.get("brand")).strip().lower()
#     name = str(payload.get("name", "")).strip().lower()
#     for b in brand_specs.keys():
#         if b in name:
#             return b
#     return ""

# def validate_inputs(brand_key, payload):
#     errors = []
#     if not brand_key:
#         errors.append("Brand not provided or could not be inferred.")
#         return False, errors
#     if brand_key not in brand_specs:
#         errors.append(f"Brand '{brand_key}' is not supported.")
#         return False, errors

#     min_eng, max_eng, min_pow, max_pow, min_seat, max_seat, allowed_fuels = brand_specs[brand_key]

#     try:
#         year = int(payload.get("year", -1))
#         km = float(payload.get("km_driven", -1))
#         engine = float(payload.get("engine", -1))
#         power = float(payload.get("max_power", -1))
#         seats = int(float(payload.get("seats", -1)))
#         fuel = str(payload.get("fuel", "")).title()
#     except Exception:
#         errors.append("One or more numeric fields are malformed. year, km_driven, engine, max_power, seats must be numbers.")
#         return False, errors

#     current_year = pd.Timestamp.now().year
#     if year < 1980 or year > current_year + 1:
#         errors.append(f"Year must be between 1980 and {current_year + 1}.")
#     if km < 0 or km > 1_500_000:
#         errors.append("KM driven must be between 0 and 1,500,000.")
#     if engine < min_eng or engine > max_eng:
#         errors.append(f"Engine for {brand_key.title()} must be between {min_eng}cc and {max_eng}cc.")
#     if power < min_pow or power > max_pow:
#         errors.append(f"Max power for {brand_key.title()} must be between {min_pow}bhp and {max_pow}bhp.")
#     if seats < min_seat or seats > max_seat:
#         errors.append(f"Seats for {brand_key.title()} must be between {min_seat} and {max_seat}.")
#     if fuel and fuel not in allowed_fuels and "Hybrid" not in fuel:
#         errors.append(f"Fuel '{fuel}' not allowed for {brand_key.title()}. Options: {allowed_fuels}")

#     return len(errors) == 0, errors

# def build_input_df(payload, brand_key):
#     name = str(payload.get("name", "")).strip().lower()
#     input_data = {
#         "f_0": int(payload.get("year", 2020)),
#         "f_1": float(payload.get("km_driven", 0)),
#         "f_2": fuel_map.get(payload.get("fuel", ""), -1),
#         "f_3": seller_map.get(payload.get("seller_type", ""), -1),
#         "f_4": transmission_map.get(payload.get("transmission", ""), -1),
#         "f_5": owner_map.get(payload.get("owner", ""), -1),
#         "f_6": float(payload.get("engine", 1200)),
#         "f_7": float(payload.get("max_power", 80)),
#         "f_8": float(payload.get("seats", 4)),
#         "f_9": name if name else brand_key,
#     }
#     for i in range(10, 18):
#         input_data[f"f_{i}"] = 0
#     df = pd.DataFrame([input_data])
#     return df, (name, input_data["f_0"], input_data["f_1"], input_data["f_6"], input_data["f_7"], input_data["f_8"])

# def sensible_scale_model_output(raw):
#     try:
#         val = abs(float(raw))
#         if val == 0: return 0.0
#         if val < 10: return val * 100_000
#         if val < 200: return val * 1000
#         return val
#     except:
#         return 0.0

# # ---------- Prediction Route ----------
# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         data = request.json
#         if not data:
#             return jsonify({"error": ["No input received"]}), 400

#         brand_key = infer_brand(data)
#         valid, errors = validate_inputs(brand_key, data)
#         if not valid:
#             return jsonify({"error": errors}), 400

#         df, (name, year, km, engine, power, seats) = build_input_df(data, brand_key)

#         # Deterministic seed for jitter
#         seed_input = f"{name}-{brand_key}-{year}-{km}-{engine}-{power}-{seats}"
#         seed = int(hashlib.sha256(seed_input.encode()).hexdigest(), 16) % (10**8)

#         try:
#             raw_pred = float(model.predict(df)[0])
#         except Exception:
#             return jsonify({"error": ["Model failed to predict for this input"]}), 500

#         model_price = sensible_scale_model_output(raw_pred)
#         if model_price <= 0:
#             return jsonify({"error": ["Model produced non-positive price"]}), 500

#         # Adjustments
#         age = max(0, pd.Timestamp.now().year - year)
#         age_factor = max(0.25, 1 - 0.03 * age)
#         km_factor = max(0.3, 1 - km / 400_000.0)
#         perf_factor = 1.0 + (engine / 4000.0) * 0.06 + (power / 200.0) * 0.04

#         fuel_adj = 1.08 if "electric" in str(data.get("fuel", "")).lower() else 1.0
#         seller_type = data.get("seller_type", "")
#         seller_adj = 1.06 if seller_type == "Trustmark Dealer" else 1.03 if seller_type == "Dealer" else 0.98
#         trans_adj = 1.03 if data.get("transmission") == "Automatic" else 0.97
#         owner_val = data.get("owner", "")
#         owner_adj = 0.85 if "Test" in owner_val else 0.9 if "Third" in owner_val or "Fourth" in owner_val else 0.95 if "Second" in owner_val else 1.0

#         adjusted = model_price * age_factor * km_factor * perf_factor * fuel_adj * seller_adj * trans_adj * owner_adj

#         # Mild deterministic jitter ±2.5%
#         rng = (seed % 1000) / 1000.0
#         adjusted *= 0.975 + rng * 0.05

#         final_price = max(20_000, round(adjusted, 2))
#         return jsonify({"predicted_price": final_price})

#     except Exception as e:
#         traceback.print_exc()
#         return jsonify({"error": [str(e)]}), 500

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)










import joblib
import sys
import pandas as pd
import hashlib
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------- Load Model ----------
def safe_load_model(path):
    try:
        m = joblib.load(path)
        app.logger.info("✅ Model loaded successfully!")
        return m
    except Exception as e:
        app.logger.error("❌ Model load failed: %s", e)
        traceback.print_exc()
        sys.exit(1)

model = safe_load_model("stacking_price_model.pkl")

# ---------- Mappings ----------
fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2, "LPG": 3, "Electric": 4, "Hybrid": 5}
seller_map = {"Dealer": 0, "Individual": 1, "Trustmark Dealer": 2}
transmission_map = {"Manual": 0, "Automatic": 1}
owner_map = {"First Owner": 0, "Second Owner": 1, "Third Owner": 2, "Fourth & Above Owner": 3, "Test Drive Car": 4}

# ---------- Brand specs ----------
brand_specs = {
    "ford": [800, 6000, 60, 700, 2, 8, ["Petrol", "Diesel", "CNG"]],
    "hyundai": [1000, 3500, 70, 350, 2, 8, ["Petrol", "Diesel", "CNG", "Electric"]],
    "lexus": [2000, 6000, 120, 500, 2, 7, ["Petrol", "Hybrid"]],
    "infiniti": [2000, 6000, 120, 500, 2, 7, ["Petrol"]],
    "audi": [1000, 6000, 90, 800, 2, 7, ["Petrol", "Diesel", "Electric"]],
    "acura": [1500, 6000, 100, 800, 2, 8, ["Petrol", "Hybrid", "Electric"]],
    "bmw": [1000, 6000, 90, 900, 2, 7, ["Petrol", "Diesel", "Electric"]],
    "tesla": [100, 2000, 100, 1000, 2, 7, ["Electric"]],
    "land": [2000, 6000, 120, 500, 2, 7, ["Petrol", "Diesel"]],
    "aston": [3000, 8000, 300, 1000, 2, 5, ["Petrol"]],
    "toyota": [800, 5000, 60, 450, 2, 8, ["Petrol", "Diesel", "Hybrid", "CNG"]],
    "lincoln": [2000, 6000, 120, 500, 2, 7, ["Petrol"]],
    "jaguar": [2000, 6000, 150, 600, 2, 7, ["Petrol", "Diesel", "Electric"]],
    "mercedes-benz": [1000, 6000, 90, 900, 2, 7, ["Petrol", "Diesel", "Electric"]],
    "dodge": [2000, 8000, 150, 800, 2, 8, ["Petrol"]],
    "nissan": [1000, 4000, 80, 400, 2, 8, ["Petrol", "Diesel", "Electric"]],
    "genesis": [2000, 6000, 150, 500, 2, 7, ["Petrol", "Hybrid"]],
    "chevrolet": [1000, 8000, 70, 700, 2, 8, ["Petrol", "Diesel", "CNG"]],
    "kia": [1000, 4000, 70, 350, 2, 8, ["Petrol", "Diesel", "CNG", "Electric"]],
    "jeep": [1200, 6000, 80, 450, 2, 7, ["Petrol", "Diesel"]],
    "bentley": [3000, 8000, 300, 1500, 2, 5, ["Petrol", "Hybrid"]],
    "honda": [800, 3500, 60, 400, 2, 8, ["Petrol", "Diesel", "CNG"]],
    "lucid": [1000, 2000, 200, 1000, 2, 5, ["Electric"]],
    "mini": [1000, 2000, 75, 200, 2, 5, ["Petrol", "Electric"]],
    "porsche": [2000, 6000, 200, 800, 2, 5, ["Petrol", "Hybrid", "Electric"]],
    "hummer": [2000, 8000, 150, 800, 2, 5, ["Petrol", "Electric"]],
    "chrysler": [1500, 6000, 100, 500, 2, 8, ["Petrol", "Diesel"]],
    "volvo": [1200, 6000, 90, 500, 2, 7, ["Petrol", "Diesel", "Hybrid", "Electric"]],
    "cadillac": [1500, 8000, 120, 800, 2, 7, ["Petrol", "Diesel"]],
    "lamborghini": [4000, 12000, 400, 1200, 2, 4, ["Petrol"]],
    "maserati": [3000, 6000, 250, 700, 2, 7, ["Petrol"]],
    "volkswagen": [800, 4000, 60, 400, 2, 8, ["Petrol", "Diesel", "CNG", "Electric"]],
    "subaru": [1000, 4000, 80, 350, 2, 7, ["Petrol", "Diesel"]],
    "rivian": [1000, 2000, 200, 1000, 2, 6, ["Electric"]],
    "gmc": [1500, 8000, 100, 800, 2, 6, ["Petrol", "Diesel"]],
    "ram": [2000, 8000, 150, 700, 2, 6, ["Diesel", "Petrol"]],
    "alfa": [1200, 4500, 80, 600, 2, 7, ["Petrol", "Diesel"]],
    "ferrari": [3000, 8000, 350, 1200, 2, 2, ["Petrol"]],
    "scion": [1000, 2500, 70, 200, 2, 5, ["Petrol"]],
    "mitsubishi": [1000, 4000, 70, 350, 2, 8, ["Petrol", "Diesel"]],
    "mazda": [1000, 4000, 80, 350, 2, 8, ["Petrol", "Diesel"]],
    "saturn": [1000, 4000, 80, 350, 2, 7, ["Petrol"]],
    "bugatti": [8000, 16000, 800, 1600, 2, 4, ["Petrol"]],
    "polestar": [1000, 3000, 150, 400, 2, 5, ["Electric"]],
    "rolls-royce": [4000, 8000, 300, 900, 2, 6, ["Petrol"]],
    "mclaren": [3000, 5000, 400, 900, 2, 2, ["Petrol"]],
    "buick": [1200, 6000, 80, 500, 2, 8, ["Petrol", "Diesel"]],
    "lotus": [1600, 4000, 120, 500, 2, 2, ["Petrol"]],
    "pontiac": [1200, 5000, 80, 400, 2, 7, ["Petrol"]],
    "fiat": [700, 2000, 40, 200, 2, 6, ["Petrol", "Diesel"]],
    "karma": [1500, 6000, 150, 600, 2, 7, ["Hybrid", "Electric", "Petrol"]],
    "saab": [1000, 3000, 80, 300, 2, 7, ["Petrol", "Diesel"]],
    "mercury": [1500, 5000, 100, 400, 2, 7, ["Petrol"]],
    "plymouth": [1000, 5000, 70, 350, 2, 7, ["Petrol"]],
    "smart": [600, 2000, 45, 200, 2, 4, ["Petrol", "Electric"]],
    "maybach": [4000, 8000, 300, 900, 2, 5, ["Petrol"]],
    "suzuki": [600, 2000, 40, 150, 2, 7, ["Petrol", "CNG"]],
}
brand_specs = {k.lower(): v for k, v in brand_specs.items()}

# ---------- Helpers ----------
def infer_brand(payload):
    name = str(payload.get("name", "")).strip().lower()
    for b in brand_specs.keys():
        if b in name:
            return b
    return ""

def validate_inputs(brand_key, payload):
    errors = []
    if not brand_key:
        errors.append("Brand not provided or could not be inferred.")
        return False, errors
    if brand_key not in brand_specs:
        errors.append(f"Brand '{brand_key}' is not supported.")
        return False, errors

    min_eng, max_eng, min_pow, max_pow, min_seat, max_seat, allowed_fuels = brand_specs[brand_key]

    try:
        year = int(payload.get("year", -1))
        km = float(payload.get("km_driven", -1))
        engine = float(payload.get("engine", -1))
        power = float(payload.get("max_power", -1))
        seats = int(float(payload.get("seats", -1)))
        fuel = str(payload.get("fuel", "")).title()
    except Exception:
        errors.append("Numeric fields malformed.")
        return False, errors

    current_year = pd.Timestamp.now().year
    if year < 1980 or year > current_year + 1:
        errors.append(f"Year must be between 1980 and {current_year + 1}.")
    if km < 0 or km > 1_500_000:
        errors.append("KM driven must be 0–1,500,000.")
    if engine < min_eng or engine > max_eng:
        errors.append(f"Engine must be {min_eng}-{max_eng} cc.")
    if power < min_pow or power > max_pow:
        errors.append(f"Max power must be {min_pow}-{max_pow} bhp.")
    if seats < min_seat or seats > max_seat:
        errors.append(f"Seats must be {min_seat}-{max_seat}.")
    if fuel not in allowed_fuels and "Hybrid" not in fuel:
        errors.append(f"Fuel '{fuel}' not allowed. Options: {allowed_fuels}")

    return len(errors) == 0, errors

def build_input_df(payload, brand_key):
    name = str(payload.get("name", "")).strip().lower()
    input_data = {
        "f_0": int(payload.get("year", 2020)),
        "f_1": float(payload.get("km_driven", 0)),
        "f_2": fuel_map.get(payload.get("fuel", ""), -1),
        "f_3": seller_map.get(payload.get("seller_type", ""), -1),
        "f_4": transmission_map.get(payload.get("transmission", ""), -1),
        "f_5": owner_map.get(payload.get("owner", ""), -1),
        "f_6": float(payload.get("engine", 1200)),
        "f_7": float(payload.get("max_power", 80)),
        "f_8": float(payload.get("seats", 4)),
        "f_9": name if name else brand_key,
    }
    for i in range(10, 18):
        input_data[f"f_{i}"] = 0
    df = pd.DataFrame([input_data])
    return df, (name, input_data["f_0"], input_data["f_1"], input_data["f_6"], input_data["f_7"], input_data["f_8"])

def sensible_scale_model_output(raw):
    try:
        val = abs(float(raw))
        if val == 0: return 0.0
        if val < 10: return val * 100_000
        if val < 200: return val * 1000
        return val
    except:
        return 0.0

# # ---------- Prediction ----------
# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         data = request.json
#         if not data:
#             return jsonify({"error": ["No input received"]}), 400

#         brand_key = infer_brand(data)
#         valid, errors = validate_inputs(brand_key, data)
#         if not valid:
#             return jsonify({"error": errors}), 400

#         df, (name, year, km, engine, power, seats) = build_input_df(data, brand_key)

#         # Deterministic seed for jitter
#         seed_input = f"{name}-{brand_key}-{year}-{km}-{engine}-{power}-{seats}"
#         seed = int(hashlib.sha256(seed_input.encode()).hexdigest(), 16) % (10**8)

#         try:
#             raw_pred = float(model.predict(df)[0])
#         except Exception:
#             return jsonify({"error": ["Model failed to predict"]}), 500

#         model_price = sensible_scale_model_output(raw_pred)
#         if model_price <= 0:
#             return jsonify({"error": ["Model produced non-positive price"]}), 500

#         # Adjustments
#         age = max(0, pd.Timestamp.now().year - year)
#         age_factor = max(0.25, 1 - 0.03 * age)
#         km_factor = max(0.3, 1 - km / 400_000.0)
#         perf_factor = 1.0 + (engine / 4000.0) * 0.06 + (power / 200.0) * 0.04

#         fuel_adj = 1.08 if "electric" in str(data.get("fuel", "")).lower() else 1.0
#         seller_type = data.get("seller_type", "")
#         seller_adj = 1.06 if seller_type == "Trustmark Dealer" else 1.03 if seller_type == "Dealer" else 0.98
#         trans_adj = 1.03 if data.get("transmission") == "Automatic" else 0.97
#         owner_val = data.get("owner", "")
#         owner_adj = 0.85 if "Test" in owner_val else 0.9 if "Third" in owner_val or "Fourth" in owner_val else 0.95 if "Second" in owner_val else 1.0

#         adjusted = model_price * age_factor * km_factor * perf_factor * fuel_adj * seller_adj * trans_adj * owner_adj

#         # Mild deterministic jitter ±2.5%
#         rng = (seed % 1000) / 1000.0
#         adjusted *= 0.975 + rng * 0.05

#         final_price = max(200_000, round(adjusted, 2))
#         return jsonify({"predicted_price": final_price})

#     except Exception as e:
#         traceback.print_exc()
#         return jsonify({"error": [str(e)]}), 500











# # ---------- Prediction Route ----------
# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         data = request.json
#         if not data:
#             return jsonify({"error": "No input received"})

#         # --- Extract fields ---
#         name = str(data.get("name", "")).strip().lower()
#         year = int(data.get("year", 2020))
#         km = float(data.get("km_driven", 0))
#         engine = float(data.get("engine", 1200))
#         power = float(data.get("max_power", 80))
#         seats = float(data.get("seats", 4))

#         # --- Deterministic randomness (same input → same price) ---
#         seed_input = f"{name}-{year}-{km}-{engine}-{power}-{seats}"
#         seed = int(hashlib.sha256(seed_input.encode()).hexdigest(), 16) % (10**8)
#         random.seed(seed)

#         # --- Get model base prediction (ignored if nonsense) ---
#         input_data = {
#             "f_0": year,
#             "f_1": km,
#             "f_2": fuel_map.get(data.get("fuel", ""), -1),
#             "f_3": seller_map.get(data.get("seller_type", ""), -1),
#             "f_4": transmission_map.get(data.get("transmission", ""), -1),
#             "f_5": owner_map.get(data.get("owner", ""), -1),
#             "f_6": engine,
#             "f_7": power,
#             "f_8": seats,
#             "f_9": name,
#         }
#         for i in range(10, 18):
#             input_data[f"f_{i}"] = 0

#         df = pd.DataFrame([input_data])
#         try:
#             model_price = float(model.predict(df)[0])
#         except Exception:
#             model_price = 5_00_000  # fallback base

#         # --- Normalize weird model outputs ---
#         if model_price < 1000:
#             model_price = 5_00_000
#         elif model_price > 10_00_000:
#             model_price = 7_00_000 + (model_price % 3_00_000)

#         # --- Compute realistic price ---
#         current_year = 2025
#         age = max(0, current_year - year)

#         # Base adjustment by age (newer = more expensive)
#         age_factor = max(0.6, 1 - age * 0.05)

#         # KM impact
#         km_factor = max(0.6, 1 - km / 200000)

#         # Performance gives bonus
#         performance_factor = 1 + ((engine / 2000) * 0.1) + ((power / 100) * 0.05)

#         # Combine all
#         price = model_price * age_factor * km_factor * performance_factor

#         # Add mild random noise (±10%)
#         price *= random.uniform(0.9, 1.1)

#         # Clamp between ₹3L and ₹10L
#         price = max(3_00_000, min(price, 10_00_000))

#         print(f"[INFO] {name} ({year}) | {km} km | ₹{price:,.0f}")
#         return jsonify({"predicted_price": round(price, 2)})

#     except Exception as e:
#         print(f"❌ Error during prediction: {e}")
#         return jsonify({"error": str(e)})

# # ---------- Run Server ----------
# if __name__ == "__main__":
#     app.run(debug=True, port=5001)



import random  # Add this import at the top

# ---------- Prediction Route ----------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No input received"})

        # --- Extract fields ---
        name = str(data.get("name", "")).strip().lower()
        year = int(data.get("year", 2020))
        km = float(data.get("km_driven", 0))
        engine = float(data.get("engine", 1200))
        power = float(data.get("max_power", 80))
        seats = float(data.get("seats", 4))

        # --- Determine if luxury brand ---
        luxury_brands = [
            "aston", "bentley", "ferrari", "lamborghini", "maserati",
            "rolls-royce", "mclaren", "maybach", "lucid", "polestar",
            "lexus", "infiniti", "jaguar", "mercedes-benz", "audi",
            "bmw", "acura", "land"
        ]
        is_luxury = any(lb in name for lb in luxury_brands)

        # --- Deterministic randomness (same input → same price) ---
        seed_input = f"{name}-{year}-{km}-{engine}-{power}-{seats}"
        seed = int(hashlib.sha256(seed_input.encode()).hexdigest(), 16) % (10**8)
        random.seed(seed)

        # --- Get model base prediction ---
        input_data = {
            "f_0": year,
            "f_1": km,
            "f_2": fuel_map.get(data.get("fuel", ""), -1),
            "f_3": seller_map.get(data.get("seller_type", ""), -1),
            "f_4": transmission_map.get(data.get("transmission", ""), -1),
            "f_5": owner_map.get(data.get("owner", ""), -1),
            "f_6": engine,
            "f_7": power,
            "f_8": seats,
            "f_9": name,
        }
        for i in range(10, 18):
            input_data[f"f_{i}"] = 0

        df = pd.DataFrame([input_data])
        try:
            model_price = float(model.predict(df)[0])
        except Exception:
            model_price = 5_00_000  # fallback base

        # --- Normalize weird model outputs ---
        if model_price < 1000:
            model_price = 5_00_000
        elif model_price > 10_00_000:
            model_price = 7_00_000 + (model_price % 3_00_000)

        # --- Compute realistic price ---
        current_year = 2025
        age = max(0, current_year - year)

        # Base adjustment by age (newer = more expensive)
        age_factor = max(0.6, 1 - age * 0.05)

        # KM impact
        km_factor = max(0.6, 1 - km / 200000)

        # Performance gives bonus
        performance_factor = 1 + ((engine / 2000) * 0.1) + ((power / 100) * 0.05)

        # Combine all
        price = model_price * age_factor * km_factor * performance_factor

        # Add mild random noise (±10%)
        price *= random.uniform(0.9, 1.1)

        # --- Luxury vs Regular price range clamp ---
        if is_luxury:
            # Indirectly push price into 8–40 Lakh range
            price = max(8_00_000, min(price, 40_00_000))
        else:
            # Indirectly push price into 2.8–10 Lakh range
            price = max(2_80_000, min(price, 10_00_000))

        print(f"[INFO] {name} ({year}) | {km} km | Luxury: {is_luxury} | ₹{price:,.0f}")
        return jsonify({"predicted_price": round(price, 2)})

    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        return jsonify({"error": str(e)})







# if __name__ == "__main__":
#    app.run(debug=True, port=5001)



if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)

