import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import {defineConfig} from 'vite';

export default defineConfig(() => {
  return {
    base: "./",
    plugins: [react(), tailwindcss()],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    build: {
      rollupOptions: {
        input: {
          main: path.resolve(__dirname, 'index.html'),
          vehicles: path.resolve(__dirname, 'vehicles.html'),
          services: path.resolve(__dirname, 'services.html'),
          wedding: path.resolve(__dirname, 'wedding-car-hire.html'),
          about: path.resolve(__dirname, 'about.html'),
          aboutIndex: path.resolve(__dirname, 'about/index.html'),
          faq: path.resolve(__dirname, 'faq.html'),
          faqIndex: path.resolve(__dirname, 'faq/index.html'),
          contact: path.resolve(__dirname, 'contact.html'),
          contactIndex: path.resolve(__dirname, 'contact/index.html'),
          privacy: path.resolve(__dirname, 'privacy-policy.html'),
          terms: path.resolve(__dirname, 'terms.html'),
          // Commercial Location Pages
          rentCarSriLanka: path.resolve(__dirname, 'rent-a-car-sri-lanka/index.html'),
          rentCarNegombo: path.resolve(__dirname, 'rent-a-car-negombo/index.html'),
          rentCarKatunayake: path.resolve(__dirname, 'rent-a-car-katunayake/index.html'),
          rentCarColombo: path.resolve(__dirname, 'rent-a-car-colombo/index.html'),
          colomboAirport: path.resolve(__dirname, 'colombo-airport-car-rental/index.html'),
          carRentalAirport: path.resolve(__dirname, 'car-rental-colombo-airport/index.html'),
          // Service Hub Pages
          selfDrive: path.resolve(__dirname, 'self-drive-car-rental-sri-lanka/index.html'),
          chauffeur: path.resolve(__dirname, 'chauffeur-car-rental-sri-lanka/index.html'),
          suvRental: path.resolve(__dirname, 'suv-rental-sri-lanka/index.html'),
          vanRental: path.resolve(__dirname, 'van-rental-sri-lanka/index.html'),
          automaticRental: path.resolve(__dirname, 'automatic-car-rental-sri-lanka/index.html'),
          weddingHire: path.resolve(__dirname, 'wedding-car-hire-sri-lanka/index.html'),
          longTerm: path.resolve(__dirname, 'long-term-car-rental-sri-lanka/index.html'),
          guide: path.resolve(__dirname, 'sri-lanka-car-rental-guide/index.html'),
          // Fleet Hub & Detail Pages
          fleet: path.resolve(__dirname, 'fleet/index.html'),
          fleetPremio: path.resolve(__dirname, 'fleet/toyota-premio/index.html'),
          fleetAllion260: path.resolve(__dirname, 'fleet/toyota-allion-260/index.html'),
          fleetAllion240: path.resolve(__dirname, 'fleet/toyota-allion-240/index.html'),
          fleetAxio: path.resolve(__dirname, 'fleet/toyota-axio/index.html'),
          fleetPrius: path.resolve(__dirname, 'fleet/toyota-prius/index.html'),
          fleetRaize: path.resolve(__dirname, 'fleet/toyota-raize/index.html'),
          fleetVezel: path.resolve(__dirname, 'fleet/honda-vezel/index.html'),
          fleetWagonR: path.resolve(__dirname, 'fleet/suzuki-wagonr/index.html'),
          fleetIst: path.resolve(__dirname, 'fleet/toyota-ist/index.html'),
          fleetFit: path.resolve(__dirname, 'fleet/honda-fit/index.html'),
          fleetAqua: path.resolve(__dirname, 'fleet/toyota-aqua/index.html'),
          fleetVitz: path.resolve(__dirname, 'fleet/toyota-vitz/index.html'),
          fleetKdh: path.resolve(__dirname, 'fleet/toyota-kdh/index.html'),
          fleetKdhFlat: path.resolve(__dirname, 'fleet/toyota-kdh-flat-roof/index.html'),
          fleetKdhHigh: path.resolve(__dirname, 'fleet/toyota-kdh-high-roof/index.html'),
          fleetToyotaHighRoof: path.resolve(__dirname, 'fleet/toyota-high-roof/index.html'),
          fleetNV300: path.resolve(__dirname, 'fleet/nissan-nv300/index.html'),
          fleetCaravan: path.resolve(__dirname, 'fleet/nissan-caravan/index.html'),
        },
      },
    },
    server: {
      // HMR is disabled in AI Studio via DISABLE_HMR env var.
      // Do not modifyâfile watching is disabled to prevent flickering during agent edits.
      hmr: process.env.DISABLE_HMR !== 'true',
      // Disable file watching when DISABLE_HMR is true to save CPU during agent edits.
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
  };
});
