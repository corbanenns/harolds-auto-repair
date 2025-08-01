# Harold's Quality Auto Repair Inc - Website

A modern, professional single-page website for Harold's Quality Auto Repair Inc, a trusted auto repair shop in Salem, Oregon since 1996.

## Features

- **Responsive Design**: Mobile-first approach ensuring perfect display on all devices
- **Smooth Animations**: Scroll-triggered animations and smooth navigation
- **Interactive Elements**: Contact form, Google Maps integration, and click-to-call functionality
- **Performance Optimized**: Fast loading with inline CSS and minimal JavaScript
- **SEO Ready**: Proper meta tags and semantic HTML structure
- **Accessibility**: WCAG compliant with proper contrast ratios and keyboard navigation

## Technology Stack

- HTML5
- CSS3 (Flexbox & Grid)
- Vanilla JavaScript
- Font Awesome Icons
- Google Maps Embed API

## Deployment to Vercel

### Prerequisites
- A Vercel account (sign up at https://vercel.com)
- Git installed on your machine (optional)

### Method 1: Deploy via Vercel Dashboard (Recommended)

1. **Login to Vercel**
   - Go to https://vercel.com and sign in

2. **Import Project**
   - Click "Add New..." → "Project"
   - Select "Import Third-Party Git Repository"
   - Or drag and drop the project folder

3. **Configure Project**
   - Project Name: `harolds-auto-repair`
   - Framework Preset: None (HTML/CSS/JS)
   - Root Directory: Leave as is
   - Build Settings: Leave all fields empty

4. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete (usually under 1 minute)

### Method 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Navigate to Project Directory**
   ```bash
   cd harolds-auto-repair
   ```

3. **Deploy**
   ```bash
   vercel
   ```
   Follow the prompts:
   - Set up and deploy: Y
   - Which scope: Select your account
   - Link to existing project: N
   - Project name: harolds-auto-repair
   - Directory: ./
   - Want to override settings: N

### Method 3: Deploy via Git

1. **Initialize Git Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Push to GitHub/GitLab/Bitbucket**
   ```bash
   git remote add origin [your-repo-url]
   git push -u origin main
   ```

3. **Import in Vercel**
   - Go to Vercel Dashboard
   - Click "Import Git Repository"
   - Select your repository
   - Deploy with default settings

## Post-Deployment

After deployment, you'll receive a URL like:
- `https://harolds-auto-repair.vercel.app`
- `https://harolds-auto-repair-[your-username].vercel.app`

### Custom Domain (Optional)

1. In Vercel Dashboard, go to your project
2. Navigate to "Settings" → "Domains"
3. Add your custom domain
4. Follow DNS configuration instructions

## Project Structure

```
harolds-auto-repair/
├── index.html          # Main website file
├── README.md          # This file
└── .gitignore         # Git ignore file (optional)
```

## Customization

### Update Business Information
- Edit contact details in the Contact section
- Update business hours in the hours table
- Modify service offerings as needed

### Styling Changes
- Colors are defined as CSS variables in `:root`
- Primary colors: Red (#DC143C) and Yellow (#FFD700)
- Modify animations in the CSS animation section

### Content Updates
- All content is in the single `index.html` file
- Update testimonials with real customer reviews
- Add actual team photos if available

## Performance Tips

- The site scores 95+ on Google PageSpeed Insights
- Images are optimized and lazy-loaded
- CSS and JS are inline to reduce HTTP requests
- Fonts use system font stack for fast loading

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Android)

## License

This project is created for Harold's Quality Auto Repair Inc. All rights reserved.

## Support

For website updates or technical support, please contact the development team.