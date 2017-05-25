#trying to push to github ---testing testing

## require gems
require 'sinatra'
require 'sqlite3'

set :public_folder, File.dirname(__FILE__) + '/static'

db = SQLite3::Database.new("students.db")
db.results_as_hash = true

# show students on the home page
get '/' do
  @students = db.execute("SELECT * FROM students")
  erb :home
end

get '/students/new' do
  erb :new_student
end

get '/students/delete' do
  erb :delete_student
end

# get '/students/campus_view' do
#   erb :campus_view
# end


# create new students via
# a form
post '/students' do
  db.execute("INSERT INTO students (name, campus, age) VALUES (?,?,?)", [params['name'], params['campus'], params['age'].to_i])
  redirect '/'
end

# delete new student via a form
post '/delete' do  
  db.execute("INSERT INTO students (campus) VALUES (?)", params['campus'])
end

# #display students at a specific campus
# post '/students' do
#   db.execute("SELECT students (name, campus, age) VALUES (?,?,?)", [params['name'], params['campus'], params['age'].to_i])
#   redirect '/'
# end


# add static resources
