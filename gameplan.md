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
- [x] Design schema on paper (tracks table: id, title, artist, duration, file_path, created_at)
- [x] Create database in PostgreSQL
- [x] Write SQLAlchemy models in `models.py`
- [x] Test connection - create one track manually in Python shell
- **Win:** You successfully inserted and queried a track from Python

### Day 3 (Wednesday): First Endpoint
- [x] Create basic Flask app structure
- [x] Implement POST /api/tracks (create a track)
- [x] Test with curl or Postman
- **Win:** You made your first API call that saves to a real database!

### Day 4 (Thursday): Read Endpoints
- [x] Implement GET /api/tracks (list all tracks)
- [x] Implement GET /api/tracks/<id> (get single track)
- [x] Add basic error handling (404 if track doesn't exist)
- **Win:** You can create and retrieve tracks via API

### Day 5 (Friday): Update & Delete
- [x] Implement PUT /api/tracks/<id> (update track)
- [x] Implement DELETE /api/tracks/<id> (delete track)
- [x] Test all CRUD operations
- **Win:** Full CRUD functionality working! You built a real API!

### Weekend 1 (Saturday): Clean Up & Docs
- [x] Add input validation (required fields, data types)
- [x] Write a clear README with API documentation
- [x] Add example curl commands
- [x] Commit and push everything
- **Win:** Your repo looks professional with good documentation

### Weekend 1 (Sunday): Rest or Catch Up
- Use this if you fell behind, or take a break!

---

## Week 2: Enhancement & Polish
**Goal:** Add tags, search, pagination, and tests

### Milestone 6: Tags Integration (Part 1)
**Target: Day 6-7**
- [x] Add tags to POST endpoint (can create track with tags)
- [x] Add tags to GET endpoints (tracks return their tags)
- [x] Update PUT endpoint to modify tags
- **Win:** Your API handles complex many-to-many relationships

### Milestone 7: Search & Pagination
**Target: Day 8-9**
- [ ] Add GET /api/tracks/search?q=query
- [ ] Implement search by title, artist, or tags
- [ ] Add pagination to GET /api/tracks (limit, offset)
- [ ] Return metadata (total count, page info)
- **Win:** Your API has useful querying capabilities and can handle large datasets

### Milestone 8: Testing
**Target: Day 10**
- [ ] Install pytest and pytest-flask
- [ ] Write 3-5 basic tests (create track, get track, 404 handling)
- [ ] Write tests for tags, search, pagination
- [ ] Aim for 10-15 total tests
- [ ] Run tests and see them pass
- **Win:** You wrote automated tests and have confidence in your code!

### Milestone 9: Deployment
**Target: Weekend 2**
- [ ] Add environment variable support (database URL, config)
- [ ] Test locally with environment variables
- [ ] Create account on Railway or Render
- [ ] Create PostgreSQL database on Railway/Render
- [ ] Deploy your Flask app
- [ ] Test your live API with curl
- [ ] Write deployment notes in README
- **Win:** YOUR APP IS LIVE ON THE INTERNET! 🎉

---

## Week 3: Professional Polish
**Goal:** Make it production-quality

### Milestone 10: Error Handling & Code Quality
**Target: Day 11-13**
- [ ] Add proper HTTP status codes everywhere
- [ ] Add error messages in JSON format
- [ ] Handle database errors gracefully
- [ ] Add docstrings to functions
- [ ] Clean up code structure (maybe split into routes.py, models.py, etc.)
- [ ] Run through everything one more time
- **Win:** Your code is clean, well-documented, and handles errors professionally

### Milestone 11: Final Documentation
**Target: Day 14**
- [ ] Polish README with clear setup instructions
- [ ] Add examples of every endpoint
- [ ] Add example JSON responses
- [ ] Document what you learned
- **Win:** Someone else could actually use your project

### Milestone 12: Bonus Features (Optional)
**Target: Day 15 or as time allows**
- [ ] Add filtering (by artist, by date added)
- [ ] Add sorting options
- [ ] Add a simple statistics endpoint
- **Win:** Going above and beyond!

### Buffer Time
**Target: Weekend 3**
- [ ] Catch up on anything incomplete
- [ ] Final testing of deployed version
- [ ] Make sure GitHub looks great
- **Win:** Project complete and portfolio-ready!

---

## Final Steps: Job Application

### Milestone 13: Resume & Cover Letter
**Target: After project completion**
- [ ] Add this project to resume with bullet points highlighting: REST API, PostgreSQL, deployment, testing
- [ ] Write cover letter mentioning specific technical skills from this project
- [ ] Connect project to Kinsol's Audio Source Identification and Parking Monitoring work
- **Win:** You're now a much stronger applicant!

### Milestone 14: Apply to Kinsol
- [ ] Submit application with updated resume and tailored cover letter
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