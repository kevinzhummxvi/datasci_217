measurements = [18, 21, 24, 19]
review_threshold_text = "20"
review_threshold = int(review_threshold_text)
total = 0
reveiw_count = 0
for measurement in measurements:
    total += measurement
    if measurement >= review_threshold:
        reveiw_count += 1
        print("Measurement:", measurement, "review")
    else:
        print("Measurement:", measurement, "within range")

mean = total / len(measurements)

# Replace this scaffold output with your calculation, loop, decision, and summary.
print("Count:", len(measurements))
print("Total:", total)
print("Mean:", mean)
print("Review count:", reveiw_count)
