import { NavLink } from 'react-router'

export function Header() {
  return (
    <header className="site-header">
      <div className="container">
        <div className="content-column">
          <NavLink to="/" className="site-title">
            Chris Fleisch
          </NavLink>
        </div>
      </div>
    </header>
  )
}
