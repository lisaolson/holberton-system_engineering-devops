#!/usr/bin/env ruby
puts ARGV[0].scan(/hb([t])\1{2,5}n/).join
