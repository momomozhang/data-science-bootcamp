# Data Analysis Workflow Guide

## Overview
This is your systematic "data analysis recipe" to follow every time you get a new dataset. The workflow is designed to be efficient, comprehensive, and stakeholder-focused.

---

## Phase 1: Data Discovery & Understanding (30-45 minutes)

### Step 1: Establish Context (10-15 minutes)
**Business Context Questions:**
- [ ] What type of data is this? (Financial, operational, survey, sensor, etc.)
- [ ] What's the business domain/industry context?
- [ ] What time period and geographic scope does it cover?
- [ ] Who collected this data and for what purpose?
- [ ] What decisions might this data inform?
- [ ] Are there known industry benchmarks or standards?

### Step 2: Technical Data Inspection (10-15 minutes)
**Data Structure Assessment:**
- [ ] How many rows and columns?
- [ ] What are the data types for each column?
- [ ] What's the grain/unit of analysis? (customer-month, country-year, transaction-level, etc.)
- [ ] Are there unique identifiers?
- [ ] What's the data freshness/recency?

**Data Quality Check:**
- [ ] Missing value patterns (random vs systematic)
- [ ] Obvious outliers or anomalies
- [ ] Data format consistency
- [ ] Duplicate records
- [ ] Logical constraints (dates, ranges, relationships)

### Step 3: Domain Knowledge Research (10-15 minutes)
- [ ] Read all available documentation (codebooks, data dictionaries)
- [ ] Understand key metrics and their business significance
- [ ] Research what "good" vs "bad" performance looks like
- [ ] Identify typical ranges, benchmarks, or targets
- [ ] Note any known seasonality or cyclical patterns

---

## Phase 2: Exploratory Data Analysis (45-90 minutes)

### Step 4: Data Profiling (15-20 minutes)
**Quantitative Variables:**
- [ ] Summary statistics (mean, median, std dev, min/max)
- [ ] Distribution shapes (normal, skewed, bimodal, uniform)
- [ ] Outlier identification (IQR method, z-scores)

**Categorical Variables:**
- [ ] Value counts and frequencies
- [ ] Category coverage (how many categories, balance)
- [ ] Unusual or unexpected categories

**Temporal Analysis (if applicable):**
- [ ] Date range coverage
- [ ] Data density over time
- [ ] Seasonal patterns or trends

### Step 5: Generate Initial Questions Using Frameworks

**Apply "5 W's + H" Method (15-20 minutes):**

**What Questions:**
- What are the key performance indicators/metrics?
- What's the typical range of values?
- What patterns are immediately visible?

**When Questions:**
- How do metrics change over time?
- Are there seasonal patterns?
- When did major shifts occur?

**Where Questions:**
- How do different regions/segments compare?
- Where do we see the best/worst performance?
- Are there geographic patterns?

**Who Questions:**
- Which entities are top/bottom performers?
- Who are the outliers and why?
- Which customer segments behave differently?

**Why Questions:**
- What might explain the patterns I'm seeing?
- Why do certain groups perform differently?
- What external factors could influence these trends?

**How Questions:**
- How are different variables related?
- How strong are the correlations?
- How do changes in one metric affect others?

### Step 6: Quick Visual Exploration (15-20 minutes)
**Essential Charts to Create:**
- [ ] Time series plots for key metrics (trends)
- [ ] Histograms for distributions
- [ ] Scatter plots for relationships between key variables
- [ ] Box plots for group comparisons
- [ ] Bar charts for categorical breakdowns
- [ ] Correlation heatmap for numeric variables

---

## Phase 3: Focused Analysis (60-120 minutes)

### Step 7: Multi-Level Analysis Using "Zoom Levels"

**Macro Level Analysis (20-30 minutes):**
- [ ] Overall market/industry trends
- [ ] High-level performance metrics
- [ ] Major shifts or inflection points
- [ ] Broad group comparisons (regions, segments, time periods)

**Meso Level Analysis (30-45 minutes):**
- [ ] Segment-by-segment detailed analysis
- [ ] Regional or categorical deep-dives
- [ ] Mid-level aggregations and patterns
- [ ] Cross-segment comparative analysis

**Micro Level Analysis (20-30 minutes):**
- [ ] Individual entity investigations
- [ ] Outlier deep-dives (what makes them different?)
- [ ] Specific time period analysis (crises, events)
- [ ] Granular relationship exploration

### Step 8: Apply "So What?" Analysis
**For Each Pattern Found, Ask:**
- [ ] Why is this happening? (Root cause analysis)
- [ ] What does this mean for the business/stakeholders?
- [ ] What actions could this insight inform?
- [ ] Who should care about this finding?
- [ ] What are the implications if this trend continues?

---

## Phase 4: Stakeholder-Driven Insights (30-60 minutes)

### Step 9: Multi-Stakeholder Perspective Analysis
**Choose 2-3 Key Stakeholder Types:**

**Executive/Strategic Level:**
- [ ] What are the competitive advantages/disadvantages?
- [ ] Where are the growth opportunities?
- [ ] What are the major strategic risks?
- [ ] What market positioning insights exist?

**Operational Level:**
- [ ] What drives operational efficiency?
- [ ] Where are the performance bottlenecks?
- [ ] How can processes be optimized?
- [ ] What resource allocation insights exist?

**Financial Level:**
- [ ] What impacts profitability or costs?
- [ ] Where should investments be focused?
- [ ] What are the ROI patterns?
- [ ] Which activities drive the most value?

### Step 10: Business Context Integration
- [ ] How do findings relate to known industry dynamics?
- [ ] Do patterns align with external events (economic cycles, regulations)?
- [ ] What competitive intelligence can be extracted?
- [ ] Are there benchmarking opportunities against competitors?

---

## Phase 5: Question Refinement & Action Planning (15-30 minutes)

### Step 11: Question Quality Assessment
**Filter Questions Based on:**
- [ ] **Answerability:** Can this be answered with available data?
- [ ] **Relevance:** Does this matter to key stakeholders?
- [ ] **Actionability:** Could this inform specific decisions or actions?
- [ ] **Specificity:** Is this concrete enough to analyze effectively?
- [ ] **Impact:** Is this important enough to invest time in?

### Step 12: Prioritization Matrix
**Rank Remaining Questions by:**

| Criteria | Weight | Scoring |
|----------|---------|---------|
| **Business Impact** | 40% | How much would answering this matter to stakeholders? |
| **Feasibility** | 30% | How easily can this be answered with current data? |
| **Urgency** | 20% | How quickly do stakeholders need this answer? |
| **Uniqueness** | 10% | Does this provide non-obvious insights? |

### Step 13: Analysis Planning
**Create Action Plan:**
- [ ] Top 3-5 priority questions to analyze
- [ ] Required data preparation steps
- [ ] Analysis methods needed
- [ ] Visualization requirements
- [ ] Timeline and resource allocation

---

## Time Allocation Guidelines

### For Standard 4-6 Hour Analysis Projects:
- **Phase 1 (Understanding):** 15% of time (~45 minutes)
- **Phase 2 (Exploration):** 35% of time (~90 minutes)
- **Phase 3 (Focused Analysis):** 35% of time (~90 minutes)
- **Phase 4 (Insights):** 15% of time (~45 minutes)

### For Quick 1-2 Hour Analysis:
- **Phase 1:** 25% (30 minutes) - More upfront context investment
- **Phase 2:** 35% (25 minutes) - Focus on highest-impact questions only
- **Phase 3:** 30% (20 minutes) - Targeted deep-dive on 2-3 key questions
- **Phase 4:** 10% (5 minutes) - Concise stakeholder-relevant insights

### For Comprehensive Multi-Day Projects:
- Add iterative cycles between phases
- Include stakeholder feedback loops
- Plan for additional data collection if needed
- Build in time for advanced statistical analysis

---

## Quality Control Checkpoints

### Red Flags That You're Off Track:
❌ **Technical Setup Overrun:** Spending >25% of time on data cleaning/setup  
❌ **Analysis Paralysis:** Analyzing everything without prioritizing impact  
❌ **Context Blindness:** Technically correct but business-irrelevant insights  
❌ **Rabbit Holes:** Getting lost in interesting but unimportant patterns  
❌ **Stakeholder Disconnect:** Beautiful analysis that nobody asked for

### Success Indicators:
✅ **Clear Business Connection:** Every insight ties to stakeholder needs  
✅ **Actionable Outcomes:** Analysis leads to specific recommendations  
✅ **Appropriate Depth:** Right level of detail for the audience  
✅ **Compelling Story:** Findings build logically toward clear conclusions  
✅ **Quality Over Quantity:** Few high-impact insights vs many trivial ones

---

## Practical Application Template

### For Your Energy Data Project:

**Phase 1 Checklist (30 minutes):**
- [ ] Understand Our World in Data context and energy policy implications
- [ ] Identify primary stakeholders (policymakers, investors, researchers)
- [ ] Review codebook for metric definitions
- [ ] Assess data completeness by country and time period

**Phase 2 Checklist (45 minutes):**
- [ ] Profile data quality and coverage
- [ ] Generate 15-20 questions using 5 W's framework
- [ ] Create basic trend charts for renewable vs fossil fuels
- [ ] Identify interesting countries/time periods for deep-dive

**Phase 3 Checklist (60 minutes):**
- [ ] Choose one country for detailed POC analysis
- [ ] Analyze macro energy transition trends
- [ ] Compare renewable adoption rates across regions
- [ ] Investigate outliers and policy impact events

**Phase 4 Checklist (30 minutes):**
- [ ] Develop policy maker insights (what works?)
- [ ] Create investment perspectives (where are opportunities?)
- [ ] Validate findings against Our World in Data visualizations

---

## Quick Reference Decision Tree

```
New Dataset Received
├── Is this familiar domain?
│   ├── Yes → Spend 15 mins on Phase 1, focus on Phase 2-3
│   └── No → Spend 30+ mins on Phase 1, research domain thoroughly
├── Is this time-sensitive analysis?
│   ├── Yes → Use 1-2 hour template, focus on top 3 questions only
│   └── No → Use standard 4-6 hour template
├── Are stakeholders clearly defined?
│   ├── Yes → Prioritize their perspective in Phase 4
│   └── No → Spend extra time in Phase 1 identifying them
└── Is this a one-time analysis or ongoing?
    ├── One-time → Focus on immediate insights
    └── Ongoing → Build reusable templates and processes
```

---

*Remember: This workflow is a guide, not a rigid process. Adapt the time allocation and depth based on your specific project needs, data complexity, and stakeholder requirements.*
