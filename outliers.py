def min_max(lst):
    return min(lst), max(lst)

def median(lst):
    n = len(lst)
    s = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    else:
        return s[mid]

def quartiles(lst):
    n = len(lst)
    s = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        lower = s[:mid]
        upper = s[mid:]
    else:
        lower = s[:mid]
        upper = s[mid+1:]
    q1 = median(lower)
    q3 = median(upper)
    return q1, q3

def iqr(lst):
    q1, q3 = quartiles(lst)
    return q3 - q1

def outliers(lst):
    q1, q3 = quartiles(lst)
    iqr_val = iqr(lst)
    lower_bound = q1 - (1.5 * iqr_val)
    upper_bound = q3 + (1.5 * iqr_val)
    return [x for x in lst if x < lower_bound or x > upper_bound]

# Example usage:
data = []
print("Minimum value:", min_max(data)[0])
print("Maximum value:", min_max(data)[1])
print("Median:", median(data))
print("First Quartile:", quartiles(data)[0])
print("Third Quartile:", quartiles(data)[1])
print("Interquartile Range:", iqr(data))
print("Outliers:", outliers(data))
