import random
import subprocess

def compile_cpp_program(source_file, output_executable):
    """Compile a C++ source file into an executable."""
    compile_command = ["g++", source_file, "-o", output_executable]
    result = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print(f"Error compiling {source_file}: {result.stderr}")
        return False
    return True

def run_cpp_program(executable, test_input=""):
    """Runs a C++ executable with a given input and returns its output."""
    try:
        process = subprocess.Popen(
            executable,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate(input=test_input)

        if process.returncode != 0:
            print(f"Error in {executable}: {error}")
            return None
        return output.strip()

    except Exception as e:
        print(f"Exception occurred while running {executable}: {e}")
        return None

def generate_test_cases(tc = 500,N = 5,mx = 7):
    """Generate test cases programmatically."""
    test_cases = []
    test_cases.append("5")
    return test_cases

def compare_program_outputs(program1_path, program2_path):
    test_cases = generate_test_cases()

    for i, test_case in enumerate(test_cases, 1):
        #print(test_case)
        # Run both programs with the current test case
        output1 = run_cpp_program(program1_path, test_case)
        output2 = run_cpp_program(program2_path, test_case)
        #print(output2,output1)
        #print("here2")
        # Check for output mismatch
        if output1 is None or output2 is None:
            print(f"Error running programs for Test Case #{i}")
        elif output1 != output2:
            print(f"Mismatch found in Test Case #{i}")
            print(f"Input: {test_case}")
            print(f"Program 1 Output: {output1}")
            print(f"Program 2 Output: {output2}")
        else:
            print(f"Test Case #{i} passed.")

# Define paths to the source files and the two programs
program1_source = "CF\\CF.cpp"
program2_source = "CF\\Correct.cpp"

# Define paths to compiled executables
program1_executable = "CF\\CF_executable"
program2_executable = "CF\\Correct_executable"

# Compile programs
if all([
    compile_cpp_program(program1_source, program1_executable),
    compile_cpp_program(program2_source, program2_executable)
]):
    # Run the comparison if all compilations succeed
    compare_program_outputs(program1_executable, program2_executable)
else:
    print("Compilation failed. Please check your source files.")
