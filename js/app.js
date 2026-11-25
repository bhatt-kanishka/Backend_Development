/* ============================================================
   EndpointCraft — SPA Application Logic
   ============================================================ */

(function () {
  'use strict';

  // --- Configuration ---
  const fileCache = (typeof EMBEDDED_CACHE !== 'undefined') ? Object.assign({}, EMBEDDED_CACHE) : {};

  // --- Marked.js Configuration ---
  if (typeof marked !== 'undefined') {
    marked.setOptions({
      highlight: function (code, lang) {
        if (typeof hljs !== 'undefined') {
          if (lang && hljs.getLanguage(lang)) {
            try { return hljs.highlight(code, { language: lang }).value; } catch (e) {}
          }
          try { return hljs.highlightAuto(code).value; } catch (e) {}
        }
        return code.replace(/</g, '&lt;').replace(/>/g, '&gt;');
      },
      breaks: false,
      gfm: true
    });
  }

  // --- Utility: Fetch file with cache + local + remote fallback ---
  async function fetchFile(path) {
    if (!path) return null;
    const cleanPath = path.replace(/^\/+/, '');
    
    // 1. Check embedded cache
    if (fileCache[cleanPath]) return fileCache[cleanPath];

    // 2. Try normalized path keys
    for (const k of Object.keys(fileCache)) {
      if (k.toLowerCase() === cleanPath.toLowerCase() || k.endsWith(cleanPath) || cleanPath.endsWith(k)) {
        return fileCache[k];
      }
    }

    // 3. Try relative local path (if running via web server in repo)
    try {
      const localRes = await fetch(encodeURI(cleanPath));
      if (localRes.ok) {
        const text = await localRes.text();
        fileCache[cleanPath] = text;
        return text;
      }
    } catch (e) {}

    // 4. Fallback to GitHub raw
    try {
      const url = `${RAW_BASE}/${encodeURI(cleanPath)}`;
      const res = await fetch(url);
      if (res.ok) {
        const text = await res.text();
        fileCache[cleanPath] = text;
        return text;
      }
    } catch (e) {
      console.warn(`Failed to fetch ${cleanPath}:`, e);
    }

    return null;
  }

  // --- Utility: Create HTML element ---
  function el(tag, attrs = {}, ...children) {
    const e = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (k === 'className') e.className = v;
      else if (k === 'innerHTML') e.innerHTML = v;
      else if (k.startsWith('on')) e.addEventListener(k.slice(2).toLowerCase(), v);
      else e.setAttribute(k, v);
    }
    children.forEach(c => {
      if (typeof c === 'string') e.appendChild(document.createTextNode(c));
      else if (c) e.appendChild(c);
    });
    return e;
  }

  // --- Build Sidebar Navigation ---
  function buildSidebarNav() {
    const labsNav = document.getElementById('labsNav');
    const theoryNav = document.getElementById('theoryNav');

    if (labsNav) {
      labsNav.innerHTML = '';
      LABS.forEach(lab => {
        const a = el('a', { className: 'nav-child', href: `#labs/${lab.id}`, 'data-id': lab.id });
        a.textContent = lab.shortTitle;
        labsNav.appendChild(a);
      });
    }

    if (theoryNav) {
      theoryNav.innerHTML = '';
      THEORY.forEach(topic => {
        const a = el('a', { className: 'nav-child', href: `#theory/${topic.id}`, 'data-id': topic.id });
        a.textContent = topic.shortTitle;
        theoryNav.appendChild(a);
      });
    }
  }

  // --- Update Active Nav ---
  function updateActiveNav(hash) {
    document.querySelectorAll('.nav-item, .nav-child').forEach(el => el.classList.remove('active'));

    const cleanHash = hash.replace(/^#/, '');
    const parts = cleanHash.split('/');
    const section = parts[0];
    const sub = parts[1];

    const parentLink = document.querySelector(`.nav-item[data-section="${section}"]`);
    if (parentLink) parentLink.classList.add('active');

    if (sub) {
      const childLink = document.querySelector(`.nav-child[data-id="${sub}"]`);
      if (childLink) childLink.classList.add('active');
    }

    // Auto-open nav groups
    document.querySelectorAll('.nav-group').forEach(g => {
      const parentSection = g.querySelector('.nav-parent')?.dataset.section;
      if (parentSection === section) g.classList.add('open');
      else if (!sub && section !== 'labs' && section !== 'theory') g.classList.remove('open');
    });
  }

  // --- Breadcrumbs ---
  function setBreadcrumbs(crumbs) {
    const bc = document.getElementById('breadcrumbs');
    if (!bc) return;
    bc.innerHTML = '';
    crumbs.forEach((c, i) => {
      if (i > 0) bc.appendChild(el('span', { className: 'sep' }, '›'));
      if (c.href) {
        bc.appendChild(el('a', { href: c.href }, c.label));
      } else {
        bc.appendChild(el('span', { className: 'current' }, c.label));
      }
    });
  }

  // --- Circular Progress Ring SVG ---
  function ringSVG(value, max, color) {
    const pct = max > 0 ? Math.min(value / max, 1) : 0;
    const r = 27;
    const circ = 2 * Math.PI * r;
    const offset = circ * (1 - pct);
    return `
      <svg viewBox="0 0 64 64">
        <circle class="ring-bg" cx="32" cy="32" r="${r}"/>
        <circle class="ring-fg" cx="32" cy="32" r="${r}"
          stroke="${color}"
          stroke-dasharray="${circ}"
          stroke-dashoffset="${offset}"/>
      </svg>
      <div class="stat-number">${value}</div>`;
  }

  // --- Render: Home/Dashboard ---
  function renderHome() {
    setBreadcrumbs([{ label: 'Dashboard' }]);

    const totalLabs = LABS.length;
    const totalTheory = THEORY.length;
    const totalTech = SYLLABUS.technologies.length;

    const html = `
      <div class="dashboard-grid">
        <div class="card info-card" style="grid-column: span 1;">
          <div class="card-header">
            <div>
              <div class="card-title">Student Information</div>
              <div class="card-subtitle">Backend Development Coursework</div>
            </div>
            <div class="card-icon">🎓</div>
          </div>
          <div class="card-body">
            <div class="info-row"><span class="info-label">Name</span><span class="info-value">${STUDENT.name}</span></div>
            <div class="info-row"><span class="info-label">SAP ID</span><span class="info-value">${STUDENT.sapId}</span></div>
            <div class="info-row"><span class="info-label">Institute</span><span class="info-value">${STUDENT.institute}</span></div>
            <div class="info-row"><span class="info-label">Semester</span><span class="info-value">${STUDENT.semester}</span></div>
            <div class="info-row"><span class="info-label">Subject</span><span class="info-value">${STUDENT.subject}</span></div>
          </div>
        </div>

        <div class="card stat-card">
          <div class="stat-ring">${ringSVG(totalLabs, 10, 'var(--accent-pink)')}</div>
          <div class="stat-info">
            <div class="stat-label">Completed</div>
            <div class="stat-title">Laboratory Experiments</div>
          </div>
        </div>

        <div class="card stat-card">
          <div class="stat-ring">${ringSVG(totalTheory, 12, 'var(--accent-teal)')}</div>
          <div class="stat-info">
            <div class="stat-label">Covered</div>
            <div class="stat-title">Theory Topics</div>
          </div>
        </div>

        <div class="card stat-card">
          <div class="stat-ring">${ringSVG(totalTech, 16, 'var(--accent-yellow)')}</div>
          <div class="stat-info">
            <div class="stat-label">Used</div>
            <div class="stat-title">Technologies</div>
          </div>
        </div>

        <a href="#labs" class="card listing-card" style="cursor:pointer;">
          <div class="listing-card-header">
            <div class="listing-card-icon">🧪</div>
            <div>
              <div class="listing-card-title">Laboratory Experiments</div>
              <div class="listing-card-desc">${totalLabs} hands-on labs covering HTML5, Express, Django, FastAPI, MongoDB and more.</div>
            </div>
          </div>
          <div class="card-link">Explore Labs →</div>
        </a>

        <a href="#theory" class="card listing-card" style="cursor:pointer;">
          <div class="listing-card-header">
            <div class="listing-card-icon">📖</div>
            <div>
              <div class="listing-card-title">Theory & Tasks</div>
              <div class="listing-card-desc">${totalTheory} topics from REST fundamentals to data modeling and Docker.</div>
            </div>
          </div>
          <div class="card-link">Explore Theory →</div>
        </a>

        <a href="#course-plan" class="card listing-card" style="cursor:pointer;">
          <div class="listing-card-header">
            <div class="listing-card-icon">📅</div>
            <div>
              <div class="listing-card-title">Course Plan & Syllabus</div>
              <div class="listing-card-desc">5 units, ${SYLLABUS.courseOutcomes.length} course outcomes, and ${totalTech} technologies.</div>
            </div>
          </div>
          <div class="card-link">View Course Plan →</div>
        </a>
      </div>`;

    document.getElementById('content').innerHTML = html;
  }

  // --- Render: Labs Listing ---
  function renderLabsList() {
    setBreadcrumbs([{ label: 'Dashboard', href: '#home' }, { label: 'Labs' }]);
    let html = '<h2 style="font-size:1.3rem;font-weight:700;margin-bottom:20px;">Laboratory Experiments</h2><div class="listing-grid">';
    LABS.forEach(lab => {
      const tags = lab.concepts.slice(0, 4).map(c => `<span class="tag">${c}</span>`).join('');
      html += `
        <a href="#labs/${lab.id}" class="listing-card">
          <div class="listing-card-header">
            <div class="listing-card-icon">${lab.icon}</div>
            <div>
              <div class="listing-card-title">${lab.title}</div>
            </div>
          </div>
          <div class="listing-card-desc">${lab.description}</div>
          <div class="listing-card-tags">${tags}</div>
        </a>`;
    });
    html += '</div>';
    document.getElementById('content').innerHTML = html;
  }

  // --- Render: Theory Listing ---
  function renderTheoryList() {
    setBreadcrumbs([{ label: 'Dashboard', href: '#home' }, { label: 'Theory' }]);
    let html = '<h2 style="font-size:1.3rem;font-weight:700;margin-bottom:20px;">Theory & Practical Tasks</h2><div class="listing-grid">';
    THEORY.forEach(topic => {
      const tags = topic.concepts.slice(0, 4).map(c => `<span class="tag">${c}</span>`).join('');
      html += `
        <a href="#theory/${topic.id}" class="listing-card">
          <div class="listing-card-header">
            <div class="listing-card-icon">${topic.icon}</div>
            <div>
              <div class="listing-card-title">${topic.title}</div>
            </div>
          </div>
          <div class="listing-card-desc">${topic.description}</div>
          <div class="listing-card-tags">${tags}</div>
        </a>`;
    });
    html += '</div>';
    document.getElementById('content').innerHTML = html;
  }

  // --- Render: Detail Page (Lab or Theory) ---
  async function renderDetail(type, id) {
    const list = type === 'labs' ? LABS : THEORY;
    const item = list.find(x => x.id === id);
    if (!item) { renderHome(); return; }

    const parentLabel = type === 'labs' ? 'Labs' : 'Theory';
    setBreadcrumbs([
      { label: 'Dashboard', href: '#home' },
      { label: parentLabel, href: `#${type}` },
      { label: item.shortTitle }
    ]);

    const content = document.getElementById('content');
    content.innerHTML = '<div class="loading">Loading content…</div>';

    // Build detail page
    let html = '<div class="detail-page">';

    // Header
    html += `<div class="detail-header">
      <h1>${item.icon} ${item.title}</h1>
      <p>${item.description}</p>
    </div>`;

    // File structure tree (if available)
    if (item.tree) {
      html += `<div class="unit-card" style="margin-bottom:20px;">
        <h3 style="font-size:0.95rem;margin-bottom:10px;">📂 File Structure Tree</h3>
        <pre style="background:var(--code-bg);color:var(--code-text);padding:14px;border-radius:var(--radius-sm);font-family:monospace;font-size:0.82rem;overflow-x:auto;"><code>${item.tree}</code></pre>
      </div>`;
    }

    // Dependencies box (for labs or modules with dependencies)
    if (item.dependencies && item.dependencies.length > 0) {
      const deps = item.dependencies.map(d => `<span class="dep-badge">${d}</span>`).join('');
      html += `<div class="deps-box">
        <h3>📦 Dependencies & Requirements</h3>
        <div class="deps-list">${deps}</div>
        ${item.runCommand ? `<div class="run-cmd">$ ${item.runCommand}</div>` : ''}
        ${item.port ? `<div style="margin-top:8px;font-size:0.82rem;color:var(--text-muted);">Port / Access: ${item.port}</div>` : ''}
      </div>`;
    }

    // README content
    html += '<div class="markdown-body" id="readmeContent"><div class="loading">Loading documentation…</div></div>';

    // File tabs (code files)
    if (item.files && item.files.length > 0) {
      html += '<div class="file-tabs-container"><div class="file-tabs-header" id="fileTabs">';
      item.files.forEach((f, i) => {
        html += `<button class="file-tab${i === 0 ? ' active' : ''}" data-idx="${i}">📄 ${f.name}</button>`;
      });
      html += '</div><div id="fileContents">';
      item.files.forEach((f, i) => {
        html += `<div class="file-tab-content${i === 0 ? ' active' : ''}" data-idx="${i}"><div class="loading">Loading ${f.name}…</div></div>`;
      });
      html += '</div></div>';
    }

    // Prev / Next navigation
    const idx = list.indexOf(item);
    const prev = idx > 0 ? list[idx - 1] : null;
    const next = idx < list.length - 1 ? list[idx + 1] : null;

    html += '<div class="prev-next">';
    if (prev) {
      html += `<a href="#${type}/${prev.id}"><span class="pn-label">← Previous</span><span class="pn-title">${prev.shortTitle}</span></a>`;
    } else {
      html += '<div></div>';
    }
    if (next) {
      html += `<a href="#${type}/${next.id}" class="pn-next"><span class="pn-label">Next →</span><span class="pn-title">${next.shortTitle}</span></a>`;
    }
    html += '</div>';

    html += '</div>';
    content.innerHTML = html;

    // Fetch and render README
    if (item.readme) {
      const readmeText = await fetchFile(item.readme);
      const readmeEl = document.getElementById('readmeContent');
      if (readmeText && readmeEl) {
        readmeEl.innerHTML = marked.parse(readmeText);
        addCopyButtons(readmeEl);
      } else if (readmeEl) {
        readmeEl.innerHTML = '<p style="color:var(--text-muted);">Documentation not available.</p>';
      }
    }

    // Fetch and render code files
    if (item.files && item.files.length > 0) {
      const tabBtns = document.querySelectorAll('#fileTabs .file-tab');
      const tabContents = document.querySelectorAll('#fileContents .file-tab-content');

      tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          tabBtns.forEach(b => b.classList.remove('active'));
          tabContents.forEach(c => c.classList.remove('active'));
          btn.classList.add('active');
          const target = tabContents[parseInt(btn.dataset.idx)];
          if (target) target.classList.add('active');
        });
      });

      item.files.forEach(async (f, i) => {
        const code = await fetchFile(f.path);
        const container = tabContents[i];
        if (!container) return;
        if (code !== null) {
          const lang = f.lang || '';
          let highlighted = '';
          try {
            highlighted = (typeof hljs !== 'undefined' && lang && hljs.getLanguage(lang))
              ? hljs.highlight(code, { language: lang }).value
              : (typeof hljs !== 'undefined' ? hljs.highlightAuto(code).value : code.replace(/</g, '&lt;').replace(/>/g, '&gt;'));
          } catch (e) {
            highlighted = code.replace(/</g, '&lt;').replace(/>/g, '&gt;');
          }
          container.innerHTML = `<div class="code-block-wrapper"><button class="copy-btn" data-code="${encodeURIComponent(code)}">Copy</button><pre><code class="hljs">${highlighted}</code></pre></div>`;
          const copyBtn = container.querySelector('.copy-btn');
          if (copyBtn) copyBtn.addEventListener('click', handleCopy);
        } else {
          container.innerHTML = '<p style="padding:20px;color:var(--text-muted);">File not available.</p>';
        }
      });
    }
  }

  // --- Render: File/Dir Path deep linking (Reference Style: #dir=/Path/&file=Readme.md) ---
  async function renderDirectFile(dir, file) {
    const cleanDir = (dir || '').replace(/^\/+/, '').replace(/\/+$/, '');
    const cleanFile = (file || '').replace(/^\/+/, '');
    const fullPath = cleanDir ? `${cleanDir}/${cleanFile}` : cleanFile;

    // Check if this path matches a known lab or theory item
    const matchedLab = LABS.find(l => l.readme === fullPath || l.path === cleanDir || l.files.some(f => f.path === fullPath));
    if (matchedLab && (!cleanFile || cleanFile.toLowerCase().includes('readme') || cleanFile === 'list.txt')) {
      renderDetail('labs', matchedLab.id);
      return;
    }

    const matchedTheory = THEORY.find(t => t.readme === fullPath || t.path === cleanDir || t.files.some(f => f.path === fullPath));
    if (matchedTheory && (!cleanFile || cleanFile.toLowerCase().includes('readme') || cleanFile === 'list.txt')) {
      renderDetail('theory', matchedTheory.id);
      return;
    }

    // Direct generic file viewer
    setBreadcrumbs([
      { label: 'Dashboard', href: '#home' },
      { label: cleanDir || 'Files' },
      { label: cleanFile || 'Overview' }
    ]);

    const content = document.getElementById('content');
    content.innerHTML = '<div class="loading">Loading file…</div>';

    const fileContent = await fetchFile(fullPath);
    if (fileContent !== null) {
      if (cleanFile.toLowerCase().endsWith('.md')) {
        content.innerHTML = `
          <div class="detail-page">
            <div class="detail-header">
              <h1>📄 ${cleanFile}</h1>
              <p>Path: <code>${fullPath}</code></p>
            </div>
            <div class="markdown-body" id="directMarkdown">${marked.parse(fileContent)}</div>
          </div>`;
        addCopyButtons(document.getElementById('directMarkdown'));
      } else {
        const lang = cleanFile.split('.').pop();
        let highlighted = '';
        try {
          highlighted = (typeof hljs !== 'undefined' && hljs.getLanguage(lang))
            ? hljs.highlight(fileContent, { language: lang }).value
            : fileContent.replace(/</g, '&lt;').replace(/>/g, '&gt;');
        } catch (e) {
          highlighted = fileContent.replace(/</g, '&lt;').replace(/>/g, '&gt;');
        }
        content.innerHTML = `
          <div class="detail-page">
            <div class="detail-header">
              <h1>📄 ${cleanFile}</h1>
              <p>Path: <code>${fullPath}</code></p>
            </div>
            <div class="file-tabs-container">
              <div class="code-block-wrapper">
                <button class="copy-btn" data-code="${encodeURIComponent(fileContent)}">Copy</button>
                <pre><code class="hljs">${highlighted}</code></pre>
              </div>
            </div>
          </div>`;
        const copyBtn = content.querySelector('.copy-btn');
        if (copyBtn) copyBtn.addEventListener('click', handleCopy);
      }
    } else {
      content.innerHTML = `
        <div class="detail-page">
          <div class="detail-header">
            <h1>📂 ${cleanDir}</h1>
            <p>File: <code>${cleanFile}</code></p>
          </div>
          <div class="unit-card">
            <p style="color:var(--text-muted);">The requested file could not be loaded. Browse through <a href="#labs">Labs</a> or <a href="#theory">Theory</a> to view all coursework.</p>
          </div>
        </div>`;
    }
  }

  // --- Render: Course Plan ---
  function renderCoursePlan() {
    setBreadcrumbs([{ label: 'Dashboard', href: '#home' }, { label: 'Course Plan' }]);
    let html = '<h2 style="font-size:1.3rem;font-weight:700;margin-bottom:20px;">📅 Course Plan — Backend Development</h2>';

    COURSE_PLAN.units.forEach((unit) => {
      const topics = unit.topics.map(t => `<li>${t}</li>`).join('');
      html += `<div class="unit-card">
        <h3>${unit.name}</h3>
        <ul>${topics}</ul>
      </div>`;
    });

    document.getElementById('content').innerHTML = html;
  }

  // --- Render: Syllabus ---
  function renderSyllabus() {
    setBreadcrumbs([{ label: 'Dashboard', href: '#home' }, { label: 'Syllabus' }]);

    const outcomes = SYLLABUS.courseOutcomes.map(co => `<li>${co}</li>`).join('');

    let techRows = '';
    SYLLABUS.technologies.forEach(t => {
      techRows += `<tr><td><strong>${t.name}</strong></td><td>${t.category}</td><td>${t.role}</td><td><span class="tag">${t.version || 'Latest'}</span></td></tr>`;
    });

    const html = `
      <h2 style="font-size:1.3rem;font-weight:700;margin-bottom:20px;">📄 Syllabus — ${SYLLABUS.subject}</h2>
      <div class="unit-card">
        <h3>Course Outcomes</h3>
        <ul>${outcomes}</ul>
      </div>
      <h3 style="font-size:1.05rem;font-weight:700;margin:20px 0 12px;color:var(--card-plum);">Technology Matrix</h3>
      <table class="tech-table">
        <thead><tr><th>Technology</th><th>Category</th><th>Role</th><th>Version</th></tr></thead>
        <tbody>${techRows}</tbody>
      </table>`;

    document.getElementById('content').innerHTML = html;
  }

  // --- Render: Index (Tabular Directory) ---
  function renderIndex() {
    setBreadcrumbs([{ label: 'Dashboard', href: '#home' }, { label: 'Coursework Index' }]);

    const totalModules = LABS.length + THEORY.length;
    let totalFiles = 0;
    LABS.forEach(l => totalFiles += (l.files ? l.files.length : 0));
    THEORY.forEach(t => totalFiles += (t.files ? t.files.length : 0));

    let html = `
      <div class="index-header">
        <h2 class="index-header-title">📋 Coursework Index & Directory</h2>
        <p class="index-header-subtitle">Comprehensive tabular directory of all practical laboratory experiments, theory architecture modules, and code files with their actual functionality.</p>
      </div>

      <div class="index-controls">
        <div class="index-search-box">
          <span class="index-search-icon">🔍</span>
          <input type="text" id="indexFilter" class="index-search-input" placeholder="Search by topic, working, technology, or path…" />
        </div>

        <div class="index-filter-tabs">
          <button class="filter-tab-btn active" data-filter="all">
            All Modules <span class="filter-count">${totalModules}</span>
          </button>
          <button class="filter-tab-btn" data-filter="lab">
            🧪 Labs <span class="filter-count">${LABS.length}</span>
          </button>
          <button class="filter-tab-btn" data-filter="theory">
            📖 Theory <span class="filter-count">${THEORY.length}</span>
          </button>
          <button class="filter-tab-btn" data-filter="files">
            📄 Code Files <span class="filter-count">${totalFiles}</span>
          </button>
        </div>
      </div>

      <!-- Modules Tabular Directory -->
      <div class="index-table-container" id="modulesTableContainer">
        <table class="index-table" id="indexModulesTable">
          <thead>
            <tr>
              <th class="col-sno">#</th>
              <th>Topic & Core Working</th>
              <th>Category</th>
              <th>Technologies</th>
              <th>Repository Path</th>
              <th style="text-align:center;">Action</th>
            </tr>
          </thead>
          <tbody>`;

    let sno = 1;

    // 1. Laboratory Experiments
    LABS.forEach(lab => {
      const conceptsPills = (lab.concepts || []).slice(0, 3).map(c => `<span class="tech-pill">${c}</span>`).join('');
      const searchData = [lab.title, lab.working || '', lab.category || '', ...(lab.concepts || []), lab.path].join(' ').toLowerCase();

      html += `
        <tr class="module-row" data-type="lab" data-search="${searchData}">
          <td class="col-sno">${sno++}</td>
          <td class="topic-cell">
            <a href="#labs/${lab.id}" class="topic-title-link">
              <span style="font-size:1.2rem;">${lab.icon}</span>
              <span>${lab.title}</span>
            </a>
            <div class="topic-working-desc">${lab.working || lab.description}</div>
          </td>
          <td>
            <span class="badge-category badge-lab">${lab.category || 'Laboratory'}</span>
          </td>
          <td>
            <div class="tech-pills">${conceptsPills}</div>
          </td>
          <td>
            <span class="path-code">${lab.path}</span>
          </td>
          <td style="text-align:center;">
            <a href="#labs/${lab.id}" class="view-btn">View Docs →</a>
          </td>
        </tr>`;
    });

    // 2. Theory Modules
    THEORY.forEach(topic => {
      const conceptsPills = (topic.concepts || []).slice(0, 3).map(c => `<span class="tech-pill">${c}</span>`).join('');
      const searchData = [topic.title, topic.working || '', topic.category || '', ...(topic.concepts || []), topic.path].join(' ').toLowerCase();

      html += `
        <tr class="module-row" data-type="theory" data-search="${searchData}">
          <td class="col-sno">${sno++}</td>
          <td class="topic-cell">
            <a href="#theory/${topic.id}" class="topic-title-link">
              <span style="font-size:1.2rem;">${topic.icon}</span>
              <span>${topic.title}</span>
            </a>
            <div class="topic-working-desc">${topic.working || topic.description}</div>
          </td>
          <td>
            <span class="badge-category badge-theory">${topic.category || 'Theory Module'}</span>
          </td>
          <td>
            <div class="tech-pills">${conceptsPills}</div>
          </td>
          <td>
            <span class="path-code">${topic.path}</span>
          </td>
          <td style="text-align:center;">
            <a href="#theory/${topic.id}" class="view-btn">View Docs →</a>
          </td>
        </tr>`;
    });

    html += `
          </tbody>
        </table>
        <div id="noModulesMatch" class="empty-table-state" style="display:none;">
          No matching coursework modules found. Try adjusting your search keywords.
        </div>
      </div>

      <!-- Code Files Tabular Directory -->
      <div class="index-table-container" id="filesTableContainer" style="display:none;">
        <table class="index-table" id="indexFilesTable">
          <thead>
            <tr>
              <th class="col-sno">#</th>
              <th>File Name & Language</th>
              <th>Actual Purpose & Functionality</th>
              <th>Module Context</th>
              <th>Path</th>
              <th style="text-align:center;">Action</th>
            </tr>
          </thead>
          <tbody>`;

    let fileSno = 1;
    const allFilesList = [];

    LABS.forEach(l => {
      (l.files || []).forEach(f => {
        allFilesList.push({ ...f, parentTitle: l.title, parentHref: `#labs/${l.id}`, parentIcon: l.icon });
      });
    });

    THEORY.forEach(t => {
      (t.files || []).forEach(f => {
        allFilesList.push({ ...f, parentTitle: t.title, parentHref: `#theory/${t.id}`, parentIcon: t.icon });
      });
    });

    allFilesList.forEach(f => {
      const langUpper = (f.lang || f.name.split('.').pop()).toUpperCase();
      const searchData = [f.name, f.purpose || '', f.parentTitle, f.path, langUpper].join(' ').toLowerCase();

      html += `
        <tr class="file-row" data-search="${searchData}">
          <td class="col-sno">${fileSno++}</td>
          <td>
            <a href="${f.parentHref}" class="topic-title-link" style="font-family:monospace;font-size:0.86rem;">
              <span>📄</span>
              <strong>${f.name}</strong>
              <span class="badge-category badge-file" style="font-size:0.68rem;padding:2px 7px;">${langUpper}</span>
            </a>
          </td>
          <td>
            <div style="font-size:0.82rem;color:var(--text-dark);">${f.purpose || 'Component implementation'}</div>
          </td>
          <td>
            <span style="font-size:0.8rem;color:var(--text-muted);">${f.parentIcon} ${f.parentTitle.split(':')[0]}</span>
          </td>
          <td>
            <span class="path-code">${f.path}</span>
          </td>
          <td style="text-align:center;">
            <a href="${f.parentHref}" class="view-btn">Inspect Code →</a>
          </td>
        </tr>`;
    });

    html += `
          </tbody>
        </table>
        <div id="noFilesMatch" class="empty-table-state" style="display:none;">
          No matching code files found.
        </div>
      </div>`;

    document.getElementById('content').innerHTML = html;

    // --- Interactive Tab & Search Logic ---
    let currentFilter = 'all';
    const filterBtns = document.querySelectorAll('.filter-tab-btn');
    const modulesContainer = document.getElementById('modulesTableContainer');
    const filesContainer = document.getElementById('filesTableContainer');
    const searchInput = document.getElementById('indexFilter');
    const moduleRows = document.querySelectorAll('.module-row');
    const fileRows = document.querySelectorAll('.file-row');
    const noModulesMatch = document.getElementById('noModulesMatch');
    const noFilesMatch = document.getElementById('noFilesMatch');

    function filterTable() {
      const q = searchInput.value.toLowerCase().trim();

      if (currentFilter === 'files') {
        modulesContainer.style.display = 'none';
        filesContainer.style.display = 'block';

        let visibleCount = 0;
        fileRows.forEach(row => {
          const match = !q || row.dataset.search.includes(q);
          row.style.display = match ? '' : 'none';
          if (match) visibleCount++;
        });
        noFilesMatch.style.display = visibleCount === 0 ? 'block' : 'none';
      } else {
        modulesContainer.style.display = 'block';
        filesContainer.style.display = 'none';

        let visibleCount = 0;
        moduleRows.forEach(row => {
          const typeMatch = (currentFilter === 'all') || (row.dataset.type === currentFilter);
          const searchMatch = !q || row.dataset.search.includes(q);
          const isVisible = typeMatch && searchMatch;
          row.style.display = isVisible ? '' : 'none';
          if (isVisible) visibleCount++;
        });
        noModulesMatch.style.display = visibleCount === 0 ? 'block' : 'none';
      }
    }

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.dataset.filter;
        filterTable();
      });
    });

    searchInput.addEventListener('input', filterTable);
  }

  // --- Copy Code Button ---
  function handleCopy(e) {
    const btn = e.currentTarget;
    const code = decodeURIComponent(btn.dataset.code);
    navigator.clipboard.writeText(code).then(() => {
      btn.textContent = 'Copied!';
      btn.classList.add('copied');
      setTimeout(() => {
        btn.textContent = 'Copy';
        btn.classList.remove('copied');
      }, 2000);
    }).catch(() => {
      btn.textContent = 'Copied!';
      setTimeout(() => { btn.textContent = 'Copy'; }, 2000);
    });
  }

  function addCopyButtons(container) {
    if (!container) return;
    container.querySelectorAll('pre').forEach(pre => {
      if (pre.closest('.code-block-wrapper')) return;
      const wrapper = el('div', { className: 'code-block-wrapper' });
      pre.parentNode.insertBefore(wrapper, pre);
      wrapper.appendChild(pre);

      const code = pre.textContent;
      const btn = el('button', {
        className: 'copy-btn',
        'data-code': encodeURIComponent(code),
        onClick: handleCopy
      }, 'Copy');
      wrapper.insertBefore(btn, pre);
    });
  }

  // --- Search (Includes File names, Titles, Concepts, and README content) ---
  function initSearch() {
    const input = document.getElementById('searchInput');
    const results = document.getElementById('searchResults');
    if (!input || !results) return;

    const allItems = [
      ...LABS.map(l => ({
        title: l.title,
        icon: l.icon,
        path: l.path,
        href: `#labs/${l.id}`,
        keywords: [l.title, l.shortTitle, ...l.concepts, l.path, fileCache[l.readme] || ''].join(' ').toLowerCase()
      })),
      ...THEORY.map(t => ({
        title: t.title,
        icon: t.icon,
        path: t.path,
        href: `#theory/${t.id}`,
        keywords: [t.title, t.shortTitle, ...t.concepts, t.path, fileCache[t.readme] || ''].join(' ').toLowerCase()
      })),
      ...LABS.flatMap(l => l.files.map(f => ({
        title: f.name,
        icon: '📄',
        path: f.path,
        href: `#labs/${l.id}`,
        keywords: [f.name, f.path, l.title, fileCache[f.path] || ''].join(' ').toLowerCase()
      }))),
      ...THEORY.flatMap(t => t.files.map(f => ({
        title: f.name,
        icon: '📄',
        path: f.path,
        href: `#theory/${t.id}`,
        keywords: [f.name, f.path, t.title, fileCache[f.path] || ''].join(' ').toLowerCase()
      }))),
      { title: 'Course Plan', icon: '📅', path: 'Course Plan', href: '#course-plan', keywords: 'course plan curriculum units syllabus outcomes' },
      { title: 'Syllabus', icon: '📄', path: 'Syllabus', href: '#syllabus', keywords: 'syllabus outcomes technologies course outcomes' },
      { title: 'Student Profile', icon: '🎓', path: 'Kanishka Bhatt', href: '#home', keywords: 'kanishka bhatt 590017366 upes backend development' }
    ];

    input.addEventListener('input', function () {
      const q = this.value.toLowerCase().trim();
      if (q.length < 2) { results.classList.remove('show'); return; }

      const matches = allItems.filter(item => item.keywords.includes(q)).slice(0, 8);

      if (matches.length === 0) {
        results.innerHTML = '<div class="search-result-item"><div>No results found</div></div>';
      } else {
        results.innerHTML = matches.map(m => `
          <a href="${m.href}" class="search-result-item">
            <span class="search-result-icon">${m.icon}</span>
            <div>
              <div class="search-result-title">${m.title}</div>
              ${m.path ? `<div class="search-result-path">${m.path}</div>` : ''}
            </div>
          </a>`).join('');
      }
      results.classList.add('show');
    });

    input.addEventListener('blur', () => { setTimeout(() => results.classList.remove('show'), 250); });
    input.addEventListener('focus', () => { if (input.value.trim().length >= 2) results.classList.add('show'); });

    results.addEventListener('click', () => { results.classList.remove('show'); input.value = ''; });
  }

  // --- Mobile Menu ---
  function initMobileMenu() {
    const hamburger = document.getElementById('hamburgerBtn');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    if (!hamburger || !sidebar || !overlay) return;

    function toggleMenu() {
      sidebar.classList.toggle('open');
      overlay.classList.toggle('show');
    }

    hamburger.addEventListener('click', toggleMenu);
    overlay.addEventListener('click', toggleMenu);

    // Close on nav click (mobile)
    sidebar.addEventListener('click', (e) => {
      if (e.target.closest('.nav-child') || (e.target.closest('.nav-item') && !e.target.closest('.nav-parent'))) {
        if (window.innerWidth <= 768) toggleMenu();
      }
    });
  }

  // --- Sidebar nav-group toggle ---
  function initNavGroups() {
    document.querySelectorAll('.nav-parent').forEach(parent => {
      parent.addEventListener('click', () => {
        const group = parent.closest('.nav-group');
        if (group) group.classList.toggle('open');
      });
    });
  }

  // --- Router ---
  function route() {
    const rawHash = location.hash || '#home';
    const cleanHash = rawHash.replace(/^#/, '');

    // Check for parameter-style deep linking (e.g. #dir=/Lab/&file=Readme.md)
    if (cleanHash.startsWith('dir=') || cleanHash.includes('&file=') || cleanHash.includes('dir=')) {
      const searchStr = cleanHash.startsWith('?') ? cleanHash.slice(1) : cleanHash;
      const params = new URLSearchParams(searchStr);
      const dir = params.get('dir') || '';
      const file = params.get('file') || '';
      renderDirectFile(dir, file);
      window.scrollTo(0, 0);
      return;
    }

    const parts = cleanHash.split('/');
    const section = parts[0];
    const sub = parts[1];

    updateActiveNav(rawHash);

    switch (section) {
      case 'home':
      case '':
        renderHome();
        break;
      case 'labs':
        sub ? renderDetail('labs', sub) : renderLabsList();
        break;
      case 'theory':
        sub ? renderDetail('theory', sub) : renderTheoryList();
        break;
      case 'course-plan':
        renderCoursePlan();
        break;
      case 'syllabus':
        renderSyllabus();
        break;
      case 'index':
        renderIndex();
        break;
      default:
        renderHome();
    }

    // Scroll to top on navigation
    window.scrollTo(0, 0);
  }

  // --- Init ---
  function init() {
    buildSidebarNav();
    initSearch();
    initMobileMenu();
    initNavGroups();

    window.addEventListener('hashchange', route);
    route();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
