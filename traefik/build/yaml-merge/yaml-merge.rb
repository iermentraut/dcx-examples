#!/usr/bin/env ruby
require 'yaml'
require 'deep_merge'

if ARGV.empty?
    puts "Usage: yaml-merge foo.yml bar.yml"
    exit
end

result = {}
ARGV.each do |file_path|
    result.deep_merge!(YAML.load_file(file_path))
end

puts result.to_yaml
