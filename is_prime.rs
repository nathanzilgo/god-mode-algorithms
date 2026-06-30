use std::io;

fn is_prime(number: u64) -> bool {
    if number <= 1 {
        return false;
    }

    for i in 2..number {
        if number % i == 0{
            return false;
        }
    }
    true
}

fn main() {
    println!("Write a number: ");

    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("failed to read line");
    
    let number: u64 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) =>  {
            println!("Please enter a valid number!");
            return;
        }
    };

    println!("Is {} prime? {}", number, is_prime(number));
}
