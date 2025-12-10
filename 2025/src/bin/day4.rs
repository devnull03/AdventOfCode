use advent2025::load_inputs;

fn main() {
    let input: Vec<String> = load_inputs("day4").unwrap();
    println!("Day 4: {} lines read", input.len());
    part1_retarded(&input);
    println!("{}", count_accessible(&input));
    // part2(&input);
}

fn get_num(arr: &[u8]) -> i32 {
    arr.iter().map(|e| if e == &b'@' { 1 } else { 0 }).sum()
}

fn part1_retarded(input: &Vec<String>) -> i32 {
    let mut running_total = 0;
    // let line_len = input[0].len();

    for line in 0..input.len() {
        // let mut start = 0;
        let range_size = 3;

        let mut top_window = line.checked_sub(1).and_then(|i| {
            input
                .get(i)
                .map(|v| v.as_bytes().windows(range_size))
        });

        let mut center_window = input
            .get(line)
            .map(|v| v.as_bytes().windows(range_size))
            .unwrap();

        let mut bottom_window = if line + 1 < input.len() {
            input
                .get(line + 1)
                .map(|v| v.as_bytes().windows(range_size))
        } else {
            None
        };

        loop {
            let mut tp_amt: i32 = 0;

            let cw = match center_window.next() {
                Some(cw) => cw,
                None => break,
            };
            tp_amt += get_num(cw);

            if let Some(tw_iter) = top_window.as_mut() {
                if let Some(tw) = tw_iter.next() {
                    tp_amt += get_num(tw);
                }
            }
            if let Some(bw_iter) = bottom_window.as_mut() {
                if let Some(bw) = bw_iter.next() {
                    tp_amt += get_num(bw);
                }
            }


            if tp_amt < 4 {
                running_total += 1
            };

            // println!("Line {} processed with tp_amt = {}", line, tp_amt);
        }
    }
    println!("{running_total}");
    running_total
}

// fn part1(input: &Vec<String>) {}

// fn part2(input: &Vec<String>) {}

fn count_accessible(input: &Vec<String>) -> usize {
    let rows = input.len();
    if rows == 0 {
        return 0;
    }

    // Trim trailing whitespace (avoid CRLF issues) and assume rectangular input
    let cols = input[0].trim_end().len();
    let grid: Vec<Vec<u8>> = input
        .iter()
        .map(|s| s.trim_end().as_bytes().to_vec())
        .collect();

    let mut running_total: usize = 0;

    for r in 0..rows {
        for c in 0..cols {
            if grid[r][c] != b'@' {
                continue;
            }

            let mut neighbors = 0;
            for dr in -1isize..=1 {
                for dc in -1isize..=1 {
                    if dr == 0 && dc == 0 {
                        continue;
                    }
                    let nr = r as isize + dr;
                    let nc = c as isize + dc;
                    if nr >= 0 && nr < rows as isize && nc >= 0 && nc < cols as isize {
                        if grid[nr as usize][nc as usize] == b'@' {
                            neighbors += 1;
                        }
                    }
                }
            }

            if neighbors < 4 {
                running_total += 1;
            }
        }
    }

    running_total
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_count_is_13() {
        let raw = vec![
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ];

        let input: Vec<String> = raw.into_iter().map(|s| s.to_string()).collect();
        // assert_eq!(part1(&input), 13);
        assert_eq!(count_accessible(&input), 13);
    }
}