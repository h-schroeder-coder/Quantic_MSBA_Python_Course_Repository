crumpet_pack_size = 6 
daily_crumpet_production = 1250
percent_crumpets_produced = 0.92

# Calculate the number of crumpets produced each day
crumpets_produced = daily_crumpet_production * percent_crumpets_produced
print(f"Crumpets produced: {crumpets_produced}")

# Calculate the number of full packs produced
full_packs_produced = crumpets_produced // crumpet_pack_size
print(f"Full packs produced: {full_packs_produced}")
print(f"Full packs produced: {int(full_packs_produced)}")

# Calculate the number of crumpets left over
leftover_crumpets = crumpets_produced % crumpet_pack_size
print(f"Leftover crumpets: {leftover_crumpets}")
print(f"Leftover crumpets: {int(leftover_crumpets)}")
