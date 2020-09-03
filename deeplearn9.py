preds = weights*input_data
error = preds - target

slope  =input_data * error * 2

print(slope)
