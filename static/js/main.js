// LifeHub - Main JavaScript
// This website is a productivity platform called LifeHub. Maintain its premium purple theme, 
// rounded cards, glassmorphism effects, dashboard layout, statistics cards, calendar, 
// tasks, notes, expenses, reminders, documents, gallery, notifications, profile, settings, 
// and admin panel. The desktop version should remain almost identical, while the mobile 
// version should provide a modern app-like experience similar to Notion, Todoist, TickTick, 
// and Google Keep. Ensure every page is fully responsive and optimized for Android, iPhone, 
// iPad, laptops, and desktops.

// Mobile menu toggle
function toggleMenu() {
    const navLinks = document.getElementById('navLinks');
    if (navLinks) {
        navLinks.classList.toggle('active');
    }
}

// Sidebar toggle (Desktop & Mobile)
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar) {
        // Check if we're on mobile (sidebar has 'active' class for mobile)
        if (window.innerWidth <= 1024) {
            sidebar.classList.toggle('active');
        } else {
            // Desktop: toggle collapsed state
            sidebar.classList.toggle('collapsed');
            
            // Update button icon
            const toggleBtn = sidebar.querySelector('.sidebar-toggle-btn i');
            if (toggleBtn) {
                if (sidebar.classList.contains('collapsed')) {
                    toggleBtn.className = 'fas fa-chevron-right';
                } else {
                    toggleBtn.className = 'fas fa-chevron-left';
                }
            }
        }
    }
}

// Loading screen
window.addEventListener('load', function() {
    const loadingScreen = document.getElementById('loadingScreen');
    if (loadingScreen) {
        setTimeout(function() {
            loadingScreen.style.opacity = '0';
            setTimeout(function() {
                loadingScreen.style.display = 'none';
            }, 500);
        }, 1000);
    }
});

// Theme toggle
function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDark);
    
    // Update icon
    const themeIcon = document.querySelector('.navbar-actions button[title="Tema"] i');
    if (themeIcon) {
        themeIcon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
    }
}

// Check saved theme
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark-mode');
}

// Task checkbox toggle
function toggleTask(element) {
    element.classList.toggle('checked');
    if (element.classList.contains('checked')) {
        element.innerHTML = '<i class="fas fa-check" style="font-size: 12px; color: white;"></i>';
        element.parentElement.classList.add('completed');
    } else {
        element.innerHTML = '';
        element.parentElement.classList.remove('completed');
    }
}

// Toast notification
function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = message;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('show');
    }, 100);
    
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 300);
    }, 3000);
}

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // Add animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);
    
    const elements = document.querySelectorAll('.feature-card, .stat-card, .glass-card');
    elements.forEach(el => {
        observer.observe(el);
    });
});

// Close mobile menu when clicking outside
document.addEventListener('click', function(e) {
    const navLinks = document.getElementById('navLinks');
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    
    if (navLinks && navLinks.classList.contains('active')) {
        if (!navLinks.contains(e.target) && !mobileBtn.contains(e.target)) {
            navLinks.classList.remove('active');
        }
    }
});

// Responsive check
function checkResponsive() {
    if (window.innerWidth <= 768) {
        document.body.classList.add('mobile');
    } else {
        document.body.classList.remove('mobile');
    }
}

window.addEventListener('resize', checkResponsive);
checkResponsive();

// Logout confirmation
function confirmLogout() {
    return confirm('Rostdan ham chiqmoqchisiz?');
}

// Rotate button - only once
function rotateButton(button) {
    if (!button.classList.contains('clicked')) {
        button.classList.add('clicked');
    }
}

// Calendar navigation
function changeMonth(direction) {
    const monthYear = document.querySelector('.calendar-nav span');
    if (monthYear) {
        const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
        let currentText = monthYear.textContent;
        let parts = currentText.split(' ');
        let monthName = parts[0];
        let year = parseInt(parts[1]);
        
        let monthIndex = months.indexOf(monthName);
        if (direction === 'prev') {
            monthIndex--;
            if (monthIndex < 0) {
                monthIndex = 11;
                year--;
            }
        } else {
            monthIndex++;
            if (monthIndex > 11) {
                monthIndex = 0;
                year++;
            }
        }
        monthYear.textContent = months[monthIndex] + ' ' + year;
    }
}

// Calendar view switching
function switchCalendarView(view, event) {
    const buttons = document.querySelectorAll('.calendar-header ~ div button');
    buttons.forEach(btn => {
        btn.classList.remove('btn-primary');
        btn.classList.add('btn-outline');
    });
    
    // Find the clicked button and make it active
    const clickedBtn = event ? event.target : this;
    if (clickedBtn) {
        clickedBtn.classList.remove('btn-outline');
        clickedBtn.classList.add('btn-primary');
    }
    
    // Here you would typically load the appropriate view
    showToast(view + ' view selected');
}

// Make calendar day clickable
document.addEventListener('DOMContentLoaded', function() {
    const calendarDays = document.querySelectorAll('.calendar-day');
    calendarDays.forEach(day => {
        day.addEventListener('click', function() {
            // Remove selected class from all days
            calendarDays.forEach(d => d.classList.remove('selected'));
            // Add selected class to clicked day
            this.classList.add('selected');
        });
    });         
});

// Show add task modal
function showAddTaskModal() {
    const modal = document.getElementById('addTaskModal');
    if (modal) {
        modal.style.display = 'flex';
        modal.style.opacity = '1';
    }
}

// Close add task modal
function closeAddTaskModal() {
    const modal = document.getElementById('addTaskModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Add task
function addTask(event) {
    event.preventDefault();
    const title = document.getElementById('taskTitle').value;
    const priority = document.getElementById('taskPriority').value;
    const dueDate = document.getElementById('taskDate').value;
    
    if (title) {
        // Create new task element
        const taskList = document.querySelector('.task-list');
        const newTask = document.createElement('div');
        newTask.className = 'task-item';
        
        const priorityClass = priority === 'high' ? 'priority-high' : priority === 'medium' ? 'priority-medium' : 'priority-low';
        const priorityText = priority.charAt(0).toUpperCase() + priority.slice(1);
        
        newTask.innerHTML = `
            <div class="task-checkbox" onclick="toggleTask(this)"></div>
            <span class="task-text">${title}</span>
            <span class="task-priority ${priorityClass}">${priorityText}</span>
            <i class="fas fa-grip-vertical" style="opacity: 0.3; margin-left: auto;"></i>
        `;
        
        taskList.prepend(newTask);
        
        // Reset form and close modal
        document.getElementById('addTaskForm').reset();
        closeAddTaskModal();
        
        showToast('Task added successfully!');
    }
}

// Show add expense modal
function showAddExpenseModal() {
    const modal = document.getElementById('addExpenseModal');
    if (modal) {
        modal.style.display = 'flex';
        modal.style.opacity = '1';
    }
}

// Close add expense modal
function closeAddExpenseModal() {
    const modal = document.getElementById('addExpenseModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Add expense - now handled by form submission, no need for JS
// The form submits directly to the server

// Show add folder modal
function showAddFolderModal() {
    const modal = document.getElementById('addFolderModal');
    if (modal) {
        modal.style.display = 'flex';
        modal.style.opacity = '1';
    }
}

// Close add folder modal
function closeAddFolderModal() {
    const modal = document.getElementById('addFolderModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Add folder
function addFolder(event) {
    event.preventDefault();
    const name = document.getElementById('folderName').value;
    
    if (name) {
        // Create new folder element
        const notesSidebar = document.querySelector('.notes-sidebar');
        const newFolder = document.createElement('div');
        newFolder.className = 'folder-item';
        newFolder.innerHTML = `
            <i class="fas fa-folder"></i>
            <span>${name}</span>
        `;
        
        // Add click event to the new folder
        newFolder.addEventListener('click', function() {
            document.querySelectorAll('.folder-item').forEach(f => f.classList.remove('active'));
            this.classList.add('active');
        });
        
        notesSidebar.appendChild(newFolder);
        
        // Reset form and close modal
        document.getElementById('addFolderForm').reset();
        closeAddFolderModal();
        
        showToast('Folder added successfully!');
    }
}

// Select folder
function selectFolder(folderId, element) {
    document.querySelectorAll('.folder-item').forEach(f => f.classList.remove('active'));
    element.classList.add('active');
    showToast('Folder selected: ' + element.querySelector('span').textContent);
}

// Show add note modal
function showAddNoteModal(folderId) {
    window.currentFolderId = folderId;
    const modal = document.getElementById('addNoteModal');
    if (modal) {
        modal.style.display = 'flex';
        modal.style.opacity = '1';
    }
}

// Close add note modal
function closeAddNoteModal() {
    const modal = document.getElementById('addNoteModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Add note
function addNote(event) {
    event.preventDefault();
    const title = document.getElementById('noteTitle').value;
    const content = document.getElementById('noteText').value;
    
    if (title) {
        // Update editor with new note
        document.getElementById('currentNoteTitle').innerHTML = '<i class="fas fa-sticky-note"></i> ' + title;
        document.getElementById('noteContent').value = content;
        
        // Reset form and close modal
        document.getElementById('addNoteForm').reset();
        closeAddNoteModal();
        
        showToast('Note added successfully!');
    }
}

// Edit current note
function editCurrentNote() {
    const noteId = document.getElementById('noteId').value;
    if (noteId) {
        viewNote(noteId);
        document.getElementById('addNoteForm').action = `/edit-note/${noteId}/`;
        showAddNoteModal();
    }
}

// Delete current note
function deleteCurrentNote() {
    const noteId = document.getElementById('noteId').value;
    if (noteId && confirm('Rostdan ham o\'chirmoqchisiz?')) {
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = `/delete-note/${noteId}/`;
        const csrf = document.createElement('input');
        csrf.type = 'hidden';
        csrf.name = 'csrfmiddlewaretoken';
        csrf.value = document.querySelector('[name=csrfmiddlewaretoken]').value;
        form.appendChild(csrf);
        document.body.appendChild(form);
        form.submit();
    }
}

// Save note
function saveNote() {
    showToast('Note saved successfully!');
}

// Filter tasks
function filterTasks(filter, event) {
    const buttons = document.querySelectorAll('.task-filters button');
    buttons.forEach(btn => {
        btn.classList.remove('btn-primary');
        btn.classList.add('btn-outline');
    });
    
    // Find the clicked button and make it active
    const clickedBtn = event ? event.target : this;
    if (clickedBtn) {
        clickedBtn.classList.remove('btn-outline');
        clickedBtn.classList.add('btn-primary');
    }
    
    // Here you would typically filter the tasks
    showToast('Showing ' + filter + ' tasks');
}

// Switch document view
function switchDocumentView(view, event) {
    const buttons = document.querySelectorAll('.main-content > div:nth-child(1) > div:nth-child(2) button');
    buttons.forEach(btn => {
        btn.classList.remove('btn-primary');
        btn.classList.add('btn-outline');
    });
    
    // Find the clicked button and make it active
    const clickedBtn = event ? event.target.closest('button') : this;
    if (clickedBtn) {
        clickedBtn.classList.remove('btn-outline');
        clickedBtn.classList.add('btn-primary');
    }
    
    // Switch view
    const grid = document.getElementById('documentsGrid');
    if (grid) {
        if (view === 'list') {
            grid.style.display = 'block';
            grid.classList.add('documents-list');
        } else {
            grid.style.display = 'grid';
            grid.classList.remove('documents-list');
        }
    }
    
    showToast(view + ' view selected');
}

// Mark single notification as read
function markAsRead(notificationId, button) {
    const notificationItem = button.closest('.task-item');
    if (notificationItem) {
        notificationItem.style.opacity = '0.6';
        button.style.display = 'none';
        showToast('Notification marked as read');
    }
}

// Delete single notification
function deleteNotification(notificationId, button) {
    if (confirm('Rostdan ham o\'chirmoqchisiz?')) {
        const notificationItem = button.closest('.task-item');
        if (notificationItem) {
            notificationItem.remove();
            showToast('Notification deleted');
        }
    }
}

// Mark all notifications as read
function markAllAsRead() {
    const notifications = document.querySelectorAll('.task-item');
    notifications.forEach(item => {
        item.style.opacity = '0.6';
        const checkBtn = item.querySelector('.notification-btn');
        if (checkBtn) {
            checkBtn.style.display = 'none';
        }
    });
    showToast('All notifications marked as read');
}

// Clear all notifications
function clearAllNotifications() {
    if (confirm('Rostdan ham barcha xabarlarni o\'chirmoqchisiz?')) {
        const notifications = document.querySelectorAll('.task-item');
        notifications.forEach(item => {
            item.remove();
        });
        showToast('All notifications cleared');
    }
}

// ===== RESPONSIVE ENHANCEMENTS =====

// Handle mobile viewport changes
function handleMobileViewport() {
    // Ensure proper viewport for mobile
    const viewport = document.querySelector('meta[name="viewport"]');
    if (viewport) {
        viewport.setAttribute('content', 'width=device-width, initial-scale=1.0, viewport-fit=cover');
    }
}

// Close sidebar when clicking outside on mobile
document.addEventListener('click', function(e) {
    const sidebar = document.getElementById('sidebar');
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    
    if (sidebar && window.innerWidth <= 1024) {
        if (sidebar.classList.contains('active') && 
            !sidebar.contains(e.target) && 
            mobileBtn && !mobileBtn.contains(e.target)) {
            sidebar.classList.remove('active');
        }
    }
});

// Handle window resize for responsive adjustments
window.addEventListener('resize', function() {
    checkResponsive();
    handleMobileViewport();
    
    // Close sidebar on resize to larger screen
    const sidebar = document.getElementById('sidebar');
    if (sidebar && window.innerWidth > 1024) {
        sidebar.classList.remove('active');
    }
});

// Touch device detection and optimization
function isTouchDevice() {
    return 'ontouchstart' in window || navigator.maxTouchPoints > 0;
}

// Add touch-friendly classes to body
document.addEventListener('DOMContentLoaded', function() {
    if (isTouchDevice()) {
        document.body.classList.add('touch-device');
    }
});

// Mobile-friendly modal handling
function handleMobileModals() {
    const modals = document.querySelectorAll('.modal-overlay');
    modals.forEach(modal => {
        // Close modal when clicking outside
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        });
    });
}

// Initialize mobile enhancements
document.addEventListener('DOMContentLoaded', function() {
    handleMobileModals();
    handleMobileViewport();
});

// Smooth scroll for mobile
function smoothScrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Handle bottom nav active state
function updateBottomNavActive() {
    const bottomNavLinks = document.querySelectorAll('.bottom-nav-menu a');
    const currentPath = window.location.pathname;
    
    bottomNavLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

// Update on page load
document.addEventListener('DOMContentLoaded', function() {
    updateBottomNavActive();
});

// ===== MOBILE SPECIFIC FUNCTIONS =====

// Mobile theme toggle (for mobile header)
function toggleMobileTheme() {
    toggleTheme();
    const themeIcon = document.querySelector('.theme-btn i');
    if (themeIcon) {
        themeIcon.className = document.body.classList.contains('dark-mode') ? 'fas fa-sun' : 'fas fa-moon';
    }
}

// Close all open sidebars and menus on mobile
function closeAllMobileMenus() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar) {
        sidebar.classList.remove('active');
    }
}

// Prevent double-tap zoom on buttons (iOS fix)
document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('button, .btn');
    buttons.forEach(btn => {
        btn.style.touchAction = 'manipulation';
    });
});

// Handle mobile form inputs
document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
        // Prevent zoom on focus for iOS
        input.addEventListener('focus', function() {
            if (window.innerWidth <= 768) {
                const viewport = document.querySelector('meta[name="viewport"]');
                if (viewport) {
                    viewport.setAttribute('content', 'width=device-width, initial-scale=1.0, viewport-fit=cover, maximum-scale=1.0, user-scalable=no');
                }
            }
        });
        
        input.addEventListener('blur', function() {
            const viewport = document.querySelector('meta[name="viewport"]');
            if (viewport) {
                viewport.setAttribute('content', 'width=device-width, initial-scale=1.0, viewport-fit=cover');
            }
        });
    });
});

// Lazy loading for images
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        if (!img.hasAttribute('loading')) {
            img.setAttribute('loading', 'lazy');
        }
    });
});

// Performance optimization - debounce resize events
function debounce(func, wait) {
    let timeout;
    return function executedFunction() {
        const later = () => {
            clearTimeout(timeout);
            func();
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply debounce to resize handler
const debouncedResize = debounce(function() {
    checkResponsive();
    handleMobileViewport();
    
    const sidebar = document.getElementById('sidebar');
    if (sidebar && window.innerWidth > 1024) {
        sidebar.classList.remove('active');
    }
}, 250);

window.addEventListener('resize', debouncedResize);