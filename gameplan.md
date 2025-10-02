# Sound Library API - 3 Week Project Plan

A REST API for managing a music/sound collection with metadata, tags, and search capabilities.

**Timeline:** 3 weeks (~1-2 hours weekdays, 3-4 hours weekends)

---

## Week 1: Foundation & Setup

### Day 1 (Monday): Environment Setup ✓
- [x] Install PostgreSQL locally
- [x] Create virtual environment for Python
- [x] Install Flask, SQLAlchemy, psycopg2
- [x] Create GitHub repo and make first commit
- **Win:** You can run `flask --version` and `psql --version`

### Day 2 (Tuesday): Database Design
- [ ] Design schema on paper (tracks table: id, title, artist, duration, file_path, created_at)
- [ ] Create database in PostgreSQL
- [ ] Write SQLAlchemy models in `models.py`
- [ ] Test connection - create one track manually in Python shell
- **Win:** You successfully inserted and queried a track from Python

### Day 3 (Wednesday): First Endpoint
- [ ] Create basic Flask app structure
- [ ] Implement POST /api/tracks (create a track)
- [ ] Test with curl or Postman
- **Win:** You made your first API call that saves to a real database!

### Day 4 (Thursday): Read Endpoints
- [ ] Implement GET /api/tracks (list all tracks)
- [ ] Implement GET /api/tracks/<id> (get single track)
- [ ] Add basic error handling (404 if track doesn't exist)
- **Win:** You can create and retrieve tracks via API

### Day 5 (Friday): Update & Delete
- [ ] Implement PUT /api/tracks/<id> (update track)
- [ ] Implement DELETE /api/tracks/<id> (delete track)
- [ ] Test all CRUD operations
- **Win:** Full CRUD functionality working! You built a real API!

### Weekend 1 (Saturday): Clean Up & Docs
- [ ] Add input validation (required fields, data types)
- [ ] Write a clear README with API documentation
- [ ] Add example curl commands
- [ ] Commit and push everything
- **Win:** Your repo looks professional with good documentation

### Weekend 1 (Sunday): Rest or Catch Up
- Use this if you fell behind, or take a break!

---

## Week 2: Enhancement & Polish

### Day 6 (Monday): Tags Feature - Part 1
- [ ] Design tags table (many-to-many relationship)
- [ ] Create SQLAlchemy model for tags and association table
- [ ] Update database schema
- **Win:** You understand and implemented a many-to-many relationship!

### Day 7 (Tuesday): Tags Feature - Part 2
- [ ] Add tags to POST endpoint (can create track with tags)
- [ ] Add tags to GET endpoints (tracks return their tags)
- [ ] Update PUT endpoint to modify tags
- **Win:** Your API handles complex relationships

### Day 8 (Wednesday): Search Functionality
- [ ] Add GET /api/tracks/search?q=query
- [ ] Implement search by title, artist, or tags
- [ ] Test various search queries
- **Win:** Your API has useful querying capabilities

### Day 9 (Thursday): Pagination
- [ ] Add pagination to GET /api/tracks (limit, offset)
- [ ] Return metadata (total count, page info)
- [ ] Test with large dataset
- **Win:** Your API can handle lots of data efficiently

### Day 10 (Friday): Basic Tests
- [ ] Install pytest and pytest-flask
- [ ] Write 3-5 basic tests (create track, get track, 404 handling)
- [ ] Run tests and see them pass
- **Win:** You wrote your first automated tests!

### Weekend 2 (Saturday): Deployment Prep
- [ ] Create requirements.txt
- [ ] Add environment variable support (database URL, config)
- [ ] Test locally with environment variables
- [ ] Write deployment notes in README
- **Win:** Your app is configurable and ready to deploy

### Weekend 2 (Sunday): Deploy!
- [ ] Create account on Railway or Render
- [ ] Create PostgreSQL database on Railway/Render
- [ ] Deploy your Flask app
- [ ] Test your live API with curl
- **Win:** YOUR APP IS LIVE ON THE INTERNET! 🎉

---

## Week 3: Professional Polish

### Day 11 (Monday): Error Handling
- [ ] Add proper HTTP status codes everywhere
- [ ] Add error messages in JSON format
- [ ] Handle database errors gracefully
- **Win:** Your API handles errors professionally

### Day 12 (Tuesday): More Tests
- [ ] Write tests for tags functionality
- [ ] Write tests for search functionality
- [ ] Write tests for error cases
- [ ] Aim for 10-15 total tests
- **Win:** Good test coverage gives you confidence

### Day 13 (Wednesday): Code Quality
- [ ] Add docstrings to functions
- [ ] Clean up code structure
- [ ] Maybe split into multiple files (routes.py, models.py, etc.)
- [ ] Run through everything one more time
- **Win:** Your code looks professional

### Day 14 (Thursday): Documentation
- [ ] Polish README with clear setup instructions
- [ ] Add examples of every endpoint
- [ ] Add screenshots or example JSON responses
- [ ] Mention what you learned
- **Win:** Someone else could actually use your project

### Day 15 (Friday): Bonus Features (Optional)
- [ ] Add filtering (by artist, by date added)
- [ ] Add sorting options
- [ ] Add a simple statistics endpoint
- **Win:** Going above and beyond!

### Weekend 3: Buffer & Polish
- [ ] Catch up on anything incomplete
- [ ] Final testing of deployed version
- [ ] Make sure GitHub looks great
- **Win:** Project complete and portfolio-ready!

---

## After Week 3: Update & Apply

### Day 16-17: Resume & Cover Letter
- [ ] Add this project to resume with bullet points highlighting: REST API, PostgreSQL, deployment, testing
- [ ] Write cover letter mentioning specific technical skills from this project
- **Win:** You're now a much stronger applicant!

### Day 18: Apply to Kinsol
- [ ] Submit application
- **Win:** You gave yourself the best shot!

---

## Tips for Success

1. **Commit often** - Every small win = git commit with clear message
2. **Don't get stuck** - If something takes >30 mins, Google it or move on and come back
3. **It's okay to fall behind** - The weekends are buffer time
4. **Test as you go** - Don't wait until "test day" to verify things work
5. **Keep it simple** - Don't add fancy features, just make it solid and working

---

## Technical Stack Summary

- **Backend:** Flask (Python)
- **Database:** PostgreSQL with SQLAlchemy ORM
- **Testing:** pytest
- **Deployment:** Railway or Render
- **Version Control:** Git/GitHub

---

## Key Skills You'll Demonstrate

✓ REST API design and implementation  
✓ Relational database design (PostgreSQL)  
✓ ORM usage (SQLAlchemy)  
✓ CRUD operations  
✓ Complex relationships (many-to-many)  
✓ Search and pagination  
✓ Testing (pytest)  
✓ Deployment to cloud platform  
✓ Environment configuration  
✓ Git version control  
✓ Technical documentation  

---

**Remember:** Every day you complete is progress. Don't aim for perfection, aim for completion. You've got this! 💪s
