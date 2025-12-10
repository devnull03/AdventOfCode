use std::{
    fs,
    io::{BufRead, Error},
};

pub fn load_inputs(day: &str) -> Result<Vec<String>, Error> {
    let mut input_lines: Vec<String> = Vec::new();

    let input_file = fs::File::open(format!("inputs/{}.txt", day))?;
    let reader = std::io::BufReader::new(input_file);

    for line in reader.lines() {
        input_lines.push(line?);
    }

    Ok(input_lines)
}

/*
use advent2025::load_inputs;

fn main() {
    let input: Vec<String> = load_inputs("dayN").unwrap();
    println!("Day N: {} lines read", input.len());
    part1(&input);
    part2(&input);
}

fn part1(input: &Vec<String>) {}

fn part2(input: &Vec<String>) {}
*/
