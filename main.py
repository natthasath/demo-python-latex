import subprocess

def update_miktex():
    try:
        # Run miktexsetup command to update MiKTeX
        subprocess.run(['miktexsetup', '-u'])

        print('MiKTeX update completed successfully.')
    except subprocess.CalledProcessError as e:
        print('MiKTeX update failed:', e)

def latex_to_pdf(tex_file_path):
    try:
        # Update MiKTeX
        update_miktex()

        # Run latexmk command to convert LaTeX to PDF
        subprocess.run(['latexmk', '-pdf', '-interaction=nonstopmode', tex_file_path])

        print('Conversion completed successfully.')
    except subprocess.CalledProcessError as e:
        print('Conversion failed:', e)

# Provide the path to your LaTeX file
tex_file_path = 'report.tex'

# Call the function to convert LaTeX to PDF
latex_to_pdf(tex_file_path)
