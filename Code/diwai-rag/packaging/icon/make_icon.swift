// Draws the DIWAI Library app icon (1024 px PNG). Run: swift make_icon.swift out.png
import AppKit

let size: CGFloat = 1024
let out = CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : "icon.png"
let image = NSImage(size: NSSize(width: size, height: size))
image.lockFocus()

// Rounded square, deep blue, inset like macOS app icons.
let inset: CGFloat = 100
let rect = NSRect(x: inset, y: inset, width: size - 2 * inset, height: size - 2 * inset)
let path = NSBezierPath(roundedRect: rect, xRadius: 185, yRadius: 185)
NSGradient(starting: NSColor(srgbRed: 0.09, green: 0.33, blue: 0.78, alpha: 1),
           ending: NSColor(srgbRed: 0.03, green: 0.16, blue: 0.45, alpha: 1))!.draw(in: path, angle: -90)

// White books symbol.
let config = NSImage.SymbolConfiguration(pointSize: 430, weight: .semibold)
    .applying(NSImage.SymbolConfiguration(paletteColors: [.white]))
if let books = NSImage(systemSymbolName: "books.vertical.fill", accessibilityDescription: nil)?
    .withSymbolConfiguration(config) {
    let s = books.size
    books.draw(in: NSRect(x: (size - s.width) / 2, y: 400, width: s.width, height: s.height))
}

// Label.
let label = "DIWAI" as NSString
let attrs: [NSAttributedString.Key: Any] = [
    .font: NSFont.systemFont(ofSize: 150, weight: .heavy),
    .foregroundColor: NSColor.white,
    .kern: 6,
]
let ls = label.size(withAttributes: attrs)
label.draw(at: NSPoint(x: (size - ls.width) / 2, y: 175), withAttributes: attrs)

image.unlockFocus()
let rep = NSBitmapImageRep(data: image.tiffRepresentation!)!
try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: out))
print("wrote \(out)")
