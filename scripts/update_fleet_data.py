import re

# ==========================================
# 1. Update fleet/index.html
# ==========================================

fleet_tiles_html = """        <!-- Sedans Category -->
        <div style="margin-bottom: 3.5rem;">
          <div style="border-bottom: 2px solid var(--color-border); padding-bottom: 0.75rem; margin-bottom: 2rem;">
            <h2 style="font-size: 1.6rem; color: var(--color-primary); margin: 0;">Executive & Touring Sedans</h2>
            <p class="text-muted" style="margin-top: 0.25rem;">Well-suited for executive travel, wedding cars, airport transfers, and relaxed island tours.</p>
          </div>

          <div class="fleet-tile-grid">
            <!-- Toyota Premio -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/toyota premio.jpg" alt="Toyota Premio Sedan Rental Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Executive Sedan</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./toyota-premio/">Toyota Premio</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Dual AC</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> Large Boot</span>
                </div>
                <p class="fleet-tile-desc">The flagship choice for executive comfort, wedding car hire, and long-distance touring with abundant passenger legroom.</p>
                <div class="fleet-tile-actions">
                  <a href="./toyota-premio/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Toyota%20Premio." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Toyota Allion 260 -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/toyota allion 260.jpg" alt="Toyota Allion 260 Rental Car Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Executive Sedan</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./toyota-allion-260/">Toyota Allion 260</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Chilled AC</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> Spacious Boot</span>
                </div>
                <p class="fleet-tile-desc">Modern styling, refined road manners, and generous luggage capacity. Exceptionally popular for Colombo Airport pickups.</p>
                <div class="fleet-tile-actions">
                  <a href="./toyota-allion-260/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Toyota%20Allion%20260." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Toyota Allion 240 -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/toyota allion 240.jpg" alt="Toyota Allion 240 Rental Car Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Classic Sedan</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./toyota-allion-240/">Toyota Allion 240</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Cold AC</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> 2–3 Bags</span>
                </div>
                <p class="fleet-tile-desc">Legendary Japanese reliability at great value. Well-suited for economical family trips, budget self-drive, and monthly leases.</p>
                <div class="fleet-tile-actions">
                  <a href="./toyota-allion-240/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Toyota%20Allion%20240." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Toyota Axio -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/toyota-axio.jpg" alt="Toyota Axio Rental Car Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Comfort Sedan</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./toyota-axio/">Toyota Axio</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Air Conditioning</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> 2 Large Bags</span>
                </div>
                <p class="fleet-tile-desc">Celebrated touring sedan known for smooth automatic dynamics, robust engineering, and comfortable multi-day road trips.</p>
                <div class="fleet-tile-actions">
                  <a href="./toyota-axio/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Toyota%20Axio." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Toyota Prius -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/toyota-prius.jpg" alt="Toyota Prius Hybrid Rental Car Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Eco Hybrid Sedan</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./toyota-prius/">Toyota Prius</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Climate AC</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> 2 Large Bags</span>
                </div>
                <p class="fleet-tile-desc">Benchmark hybrid engineering delivering whisper-quiet cruising and superb fuel economy for island-wide travel.</p>
                <div class="fleet-tile-actions">
                  <a href="./toyota-prius/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Toyota%20Prius." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>
          </div>
        </div>

        <!-- SUVs & Crossovers Category -->
        <div style="margin-bottom: 3.5rem;">
          <div style="border-bottom: 2px solid var(--color-border); padding-bottom: 0.75rem; margin-bottom: 2rem;">
            <h2 style="font-size: 1.6rem; color: var(--color-primary); margin: 0;">SUVs & Crossovers</h2>
            <p class="text-muted" style="margin-top: 0.25rem;">Higher ground clearance and elevated road vision for national parks, coastal retreats, and hill roads.</p>
          </div>

          <div class="fleet-tile-grid">
            <!-- Honda Vezel -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/honda-vezel.jpg" alt="Honda Vezel Crossover SUV Rental Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Crossover SUV</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./honda-vezel/">Honda Vezel</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Climate AC</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> High Clearance</span>
                </div>
                <p class="fleet-tile-desc">Modern crossover styling, responsive acceleration, and elevated seating. A versatile SUV for scenic hill country expeditions.</p>
                <div class="fleet-tile-actions">
                  <a href="./honda-vezel/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Honda%20Vezel." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Toyota Raize -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/toyota-raize.jpg" alt="Toyota Raize Compact SUV Rental Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Compact SUV</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./toyota-raize/">Toyota Raize</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Climate AC</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> High Stance</span>
                </div>
                <p class="fleet-tile-desc">Dynamic compact SUV with generous ground clearance, bold design, and nimble handling for both urban streets and mountain roads.</p>
                <div class="fleet-tile-actions">
                  <a href="./toyota-raize/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Toyota%20Raize." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>
          </div>
        </div>

        <!-- Compact & Economy Cars -->
        <div style="margin-bottom: 3.5rem;">
          <div style="border-bottom: 2px solid var(--color-border); padding-bottom: 0.75rem; margin-bottom: 2rem;">
            <h2 style="font-size: 1.6rem; color: var(--color-primary); margin: 0;">Compact & Economy Hatchbacks</h2>
            <p class="text-muted" style="margin-top: 0.25rem;">Effortless parking, outstanding fuel mileage, and budget-friendly daily or monthly rates.</p>
          </div>

          <div class="fleet-tile-grid">
            <!-- Suzuki WagonR -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/suzuki-wagonr.jpg" alt="Suzuki WagonR Economy Car Rental Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Economy Compact</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./suzuki-wagonr/">Suzuki WagonR</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 4 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Air Conditioning</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> Tall Headroom</span>
                </div>
                <p class="fleet-tile-desc">Sri Lanka's favorite city and beach runabout. Surprisingly tall cabin headroom, easy parking, and high fuel efficiency.</p>
                <div class="fleet-tile-actions">
                  <a href="./suzuki-wagonr/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Suzuki%20WagonR." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Toyota IST -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/toyota-ist.jpg" alt="Toyota IST Compact Car Rental Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Compact Hatchback</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./toyota-ist/">Toyota IST</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Air Conditioning</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> Easy Parking</span>
                </div>
                <p class="fleet-tile-desc">Compact Japanese hatchback with solid chassis dynamics, responsive steering, and great air conditioning for couples.</p>
                <div class="fleet-tile-actions">
                  <a href="./toyota-ist/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Toyota%20IST." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Honda Fit -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/honda-fit.jpg" alt="Honda Fit Hatchback Rental Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Compact Hatchback</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./honda-fit/">Honda Fit</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Air Conditioning</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> Magic Seats</span>
                </div>
                <p class="fleet-tile-desc">Intelligent space packaging, versatile cargo space, and high fuel efficiency for self-drive island adventures.</p>
                <div class="fleet-tile-actions">
                  <a href="./honda-fit/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Honda%20Fit." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Toyota Aqua -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/toyota-aqua.jpg" alt="Toyota Aqua Hybrid Rental Car Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Hybrid Hatchback</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./toyota-aqua/">Toyota Aqua</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Air Conditioning</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> High Hybrid MPG</span>
                </div>
                <p class="fleet-tile-desc">Superior hybrid fuel economy and agile dimensions. Ideal for budget-conscious self-drive travel and coastal exploration.</p>
                <div class="fleet-tile-actions">
                  <a href="./toyota-aqua/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Toyota%20Aqua." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Toyota Vitz -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/toyota-vitz.jpg" alt="Toyota Vitz Compact City Car Rental Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Compact Hatchback</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./toyota-vitz/">Toyota Vitz</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Automatic</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 5 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Air Conditioning</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> Easy Parking</span>
                </div>
                <p class="fleet-tile-desc">Agile city hatchback with effortless handling, rapid cooling air conditioning, and budget-friendly rental rates.</p>
                <div class="fleet-tile-actions">
                  <a href="./toyota-vitz/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Toyota%20Vitz." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>
          </div>
        </div>

        <!-- Passenger Vans Category -->
        <div>
          <div style="border-bottom: 2px solid var(--color-border); padding-bottom: 0.75rem; margin-bottom: 2rem;">
            <h2 style="font-size: 1.6rem; color: var(--color-primary); margin: 0;">Group & Family Passenger Vans</h2>
            <p class="text-muted" style="margin-top: 0.25rem;">Well-suited for extended family vacations, tour groups, wedding parties, and corporate transfers.</p>
          </div>

          <div class="fleet-tile-grid">
            <!-- Toyota KDH -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/toyota-kdh-1.jpg" alt="Toyota KDH Passenger Van Rental Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Passenger Van (9–14 Seats)</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./toyota-kdh/">Toyota KDH</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Auto / Manual</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 9–14 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Dual Line AC</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> Large Luggage</span>
                </div>
                <p class="fleet-tile-desc">The gold standard for group travel in Sri Lanka. Spacious reclining seating, dual-line AC, and abundant luggage room.</p>
                <div class="fleet-tile-actions">
                  <a href="./toyota-kdh/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Toyota%20KDH." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Nissan NV300 -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/nissan-nv300.webp" alt="Nissan NV300 Passenger Van Hire Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Multi-Passenger Van</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./nissan-nv300/">Nissan NV300</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Manual / Auto</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 8–9 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Dual Line AC</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> Large Cargo</span>
                </div>
                <p class="fleet-tile-desc">Modern 8-9 passenger van with premium styling, individual seating comfort, dual AC, and expansive luggage volume for family tours.</p>
                <div class="fleet-tile-actions">
                  <a href="./nissan-nv300/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Nissan%20NV300." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>

            <!-- Nissan Caravan -->
            <article class="fleet-tile">
              <div class="fleet-tile-media">
                <img src="../assets/images/fleet/nissan-caravan.jpg" alt="Nissan Caravan Group Touring Van Sri Lanka" loading="lazy" width="600" height="380">
                <span class="fleet-tile-badge">Touring Van (10–14 Seats)</span>
              </div>
              <div class="fleet-tile-body">
                <h3 class="fleet-tile-title"><a href="./nissan-caravan/">Nissan Caravan</a></h3>
                <div class="fleet-tile-specs">
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg> Auto / Manual</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 10–14 Seats</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 12h18"></path></svg> Dual Line AC</span>
                  <span class="fleet-tile-pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg> High Capacity</span>
                </div>
                <p class="fleet-tile-desc">High-roof passenger van engineered for group touring, hotel shuttles, and long-distance travel with dual AC and huge cargo capacity.</p>
                <div class="fleet-tile-actions">
                  <a href="./nissan-caravan/" class="btn btn-outline btn-sm">View Details</a>
                  <a href="https://wa.me/94777193915?text=Hello%20KS%20Rent%20a%20Car%2C%20I%20would%20like%20to%20enquire%20about%20the%20Nissan%20Caravan." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>
          </div>
        </div>"""

form_dropdown_options = """                  <option value="Toyota Premio">Toyota Premio (Executive Sedan)</option>
                  <option value="Toyota Allion 260">Toyota Allion 260 (Executive Sedan)</option>
                  <option value="Toyota Allion 240">Toyota Allion 240 (Classic Sedan)</option>
                  <option value="Toyota Axio">Toyota Axio (Comfort Sedan)</option>
                  <option value="Toyota Prius">Toyota Prius (Eco Hybrid Sedan)</option>
                  <option value="Honda Vezel">Honda Vezel (Crossover SUV)</option>
                  <option value="Toyota Raize">Toyota Raize (Compact SUV)</option>
                  <option value="Suzuki WagonR">Suzuki WagonR (Economy Compact)</option>
                  <option value="Toyota IST">Toyota IST (Compact Hatchback)</option>
                  <option value="Honda Fit">Honda Fit (Compact Hatchback)</option>
                  <option value="Toyota Aqua">Toyota Aqua (Hybrid Hatchback)</option>
                  <option value="Toyota Vitz">Toyota Vitz (Compact Hatchback)</option>
                  <option value="Toyota KDH">Toyota KDH (Passenger Van 9–14 Seats)</option>
                  <option value="Nissan NV300">Nissan NV300 (Passenger Van 8–9 Seats)</option>
                  <option value="Nissan Caravan">Nissan Caravan (Touring Van 10–14 Seats)</option>"""

with open("fleet/index.html", "r", encoding="utf-8") as f:
    fleet_html = f.read()

# Replace description meta
fleet_html = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Explore our rental vehicle fleet in Sri Lanka. Toyota Premio, Allion 260 & 240, Axio, Prius, Honda Vezel, Raize, Suzuki WagonR, IST, Fit, Aqua, Vitz, and KDH passenger vans.">',
    fleet_html,
    count=1
)

# Replace the inner content between <section class="section" id="fleetGrid"><div class="container"> and </div></section>
grid_pattern = r'(<section class="section" id="fleetGrid">\s*<div class="container">)(.*?)(</div>\s*</section>\s*<!-- Rental Enquiry Section -->)'
match = re.search(grid_pattern, fleet_html, re.DOTALL)
if match:
    fleet_html = fleet_html[:match.start(2)] + "\n" + fleet_tiles_html + "\n      " + fleet_html[match.end(2):]
    print("Replaced fleetGrid in fleet/index.html")
else:
    print("WARNING: Could not find fleetGrid match in fleet/index.html")

# Replace dropdown in fleet/index.html
select_pattern = r'(<select id="vehicleSelect" name="vehicle_required" class="form-select" required>)(.*?)(</select>)'
match_sel = re.search(select_pattern, fleet_html, re.DOTALL)
if match_sel:
    fleet_html = fleet_html[:match_sel.start(2)] + "\n" + form_dropdown_options + "\n                " + fleet_html[match_sel.end(2):]
    print("Replaced vehicle dropdown in fleet/index.html")
else:
    print("WARNING: Could not find select in fleet/index.html")

with open("fleet/index.html", "w", encoding="utf-8") as f:
    f.write(fleet_html)
print("Updated fleet/index.html successfully!")
