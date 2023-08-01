#!/usr/bin/env ruby
def extract_info(line)
  sender = line.match(/\[from:(\S+)\]/)&.captures&.first
  receiver = line.match(/\[to:(\S+)\]/)&.captures&.first
  flags = line.match(/\[flags:(.*?)\]/)&.captures&.first

  "#{sender},#{receiver},#{flags}"
end
if ARGV.empty?
  puts "Please provide the log file."
else
  log_file_path = ARGV[0]

  File.readlines(log_file_path).each do |line|
    if line.include?("SMS")
      result = extract_info(line)
      puts result unless result.nil?
    end
  end
end
