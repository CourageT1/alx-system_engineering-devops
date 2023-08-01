#!/usr/bin/env ruby
def match_phone_number(input)
  pattern = /^\d{10}$/
  return input.match?(pattern)
end

if ARGV.empty?
  puts "Please provide an argument."
else
  input_argument = ARGV[0]
  if match_phone_number(input_argument)
    puts input_argument
  else
    puts "Invalid phone number."
  end
end
