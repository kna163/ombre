GRAPHICS_DIR = src/graphics/

all: colors data data-complex

colors: 
	cd src/graphics/; python3 gen_colors.py .
data:
	echo "Making synthetic data"

data-complex:
	echo "fetching"


clean:
