use std::{fs, io::{BufRead, Error}};

pub fn load_inputs(day: &str) -> Result<Vec<String>, Error> {
	let mut input_lines: Vec<String> = Vec::new();

	let input_file = fs::File::open(format!("inputs/{}.txt", day))?;
	let reader = std::io::BufReader::new(input_file);
	
	for line in reader.lines() {
		input_lines.push(line?);
	}
	
	Ok(input_lines)
}

