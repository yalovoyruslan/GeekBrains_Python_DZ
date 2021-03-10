import utils
import sys

a = sys.argv
print(*utils.currency_rates(a[1]))
