package com.example;

import junit.framework.TestCase;
import org.junit.Test;

public class CalculatorTest extends TestCase {

    private final Calculator calculator = new Calculator();

    @Test
    public void testAdd() {
        assertEquals(5, calculator.add(2, 3));
        System.out.println("Running testAdd");
    }

    @Test
    public void testSubtract() {
        System.out.println("Running testSubtract");
        assertEquals(1, calculator.subtract(3, 2));
    }
}