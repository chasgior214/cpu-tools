# Progress bars

from progress.bar import ChargingBar # Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar, IncrementalBar, PixelBar, ShadyBar
import time

total_iterations = 100

bar = ChargingBar('Processing', max=total_iterations)

for i in range(total_iterations):
    time.sleep(0.01)
    bar.next()

bar.finish()

print("Processing complete.")

from progress.spinner import Spinner # Spinner, PieSpinner, MoonSpinner, LineSpinner, PixelSpinner 
start_time = time.time()
spinner = Spinner('Loading ')
while time.time() - start_time < 5:
    time.sleep(0.1)
    spinner.next()
spinner.finish()