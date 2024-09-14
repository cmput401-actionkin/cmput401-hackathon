import { useState } from 'react';
import styles from './Navbar.module.css';

function Navbar() {
  const [isActive, setIsActive] = useState(false);

  const toggleActiveClass = () => {
    setIsActive(!isActive);
  };

  return (
    <div className="App">
      <header className="App-header">
        <nav className={styles.navbar}>
            
          {/* Logo */}
          <a href='#home' className={styles.logo}>Jobtective</a>

          {/* Search Bar */}
          <form className={styles.searchForm} onSubmit={(e) => e.preventDefault()}>
            <input 
              type="text" 
              placeholder="Job Title" 
              className={styles.searchInput} 
            />
            <button type="submit" className={styles.searchButton}>Search</button>
          </form>

          {/* Hamburger Menu */}
          <div className={`${styles.hamburger} ${isActive ? styles.active : ''}`} onClick={toggleActiveClass}>
            <span className={styles.bar}></span>
            <span className={styles.bar}></span>
            <span className={styles.bar}></span>
          </div>
        </nav>
      </header>
    </div>
  );
}

export default Navbar;
