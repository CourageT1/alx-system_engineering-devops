#!/usr/bin/env ruby
def match_capital_letters(input)
  pattern = /[A-Z]/
  return input.scan(pattern).join
end
if ARGV.empty?
  puts "Please provide an argument."
else
  input_argument = ARGV[0]
  result = match_capital_letters(input_argument)

  if result.empty?
    puts "No capital letters found."
  else
    puts result
  end
end
